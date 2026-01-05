import pandas as pd
import mysql.connector
from dateutil import parser
import logging

# -------------------- Logging Setup --------------------
logging.basicConfig(
    filename="etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -------------------- MySQL Connection --------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="fleximart"
)
cursor = conn.cursor()

# -------------------- Helper Functions --------------------


def standardize_phone(phone):
    if pd.isna(phone):
        return None
    digits = ''.join(filter(str.isdigit, str(phone)))
    return f"+91-{digits[-10:]}" if len(digits) >= 10 else None


def parse_date(value):
    try:
        return parser.parse(str(value)).date()
    except:
        return None


# -------------------- Data Quality Counters --------------------
report = {
    "customers": {"processed": 0, "duplicates": 0, "missing": 0},
    "products": {"processed": 0, "duplicates": 0, "missing": 0},
    "sales": {"processed": 0, "duplicates": 0, "missing": 0}
}

# -------------------- Extract --------------------
customers = pd.read_csv("../data/customers_raw.csv")
products = pd.read_csv("../data/products_raw.csv")
sales = pd.read_csv("../data/sales_raw.csv")

# -------------------- Transform: Customers --------------------
report["customers"]["processed"] = len(customers)
customers.drop_duplicates(inplace=True)
report["customers"]["duplicates"] = report["customers"]["processed"] - \
    len(customers)

customers.dropna(subset=["email"], inplace=True)
customers["phone"] = customers["phone"].apply(standardize_phone)
customers["registration_date"] = customers["registration_date"].apply(
    parse_date)

# -------------------- Load: Customers --------------------
for _, row in customers.iterrows():
    cursor.execute("""
        INSERT IGNORE INTO customers
        (first_name, last_name, email, phone, city, registration_date)
        VALUES (%s,%s,%s,%s,%s,%s)
    """, tuple(row))

conn.commit()

# -------------------- Transform: Products --------------------
report["products"]["processed"] = len(products)
products.drop_duplicates(inplace=True)
products["category"] = products["category"].str.title()
products["price"].fillna(products["price"].median(), inplace=True)
products["stock_quantity"].fillna(0, inplace=True)

# -------------------- Load: Products --------------------
for _, row in products.iterrows():
    cursor.execute("""
        INSERT INTO products
        (product_name, category, price, stock_quantity)
        VALUES (%s,%s,%s,%s)
    """, tuple(row))

conn.commit()

# -------------------- Transform: Sales --------------------
report["sales"]["processed"] = len(sales)
sales.drop_duplicates(inplace=True)
sales["order_date"] = sales["order_date"].apply(parse_date)
sales.dropna(subset=["customer_id", "product_id"], inplace=True)

# -------------------- Load: Orders & Order Items --------------------
for _, row in sales.iterrows():
    cursor.execute("""
        INSERT INTO orders (customer_id, order_date, total_amount)
        VALUES (%s,%s,%s)
    """, (row["customer_id"], row["order_date"], row["total_amount"]))
    order_id = cursor.lastrowid

    cursor.execute("""
        INSERT INTO order_items
        (order_id, product_id, quantity, unit_price, subtotal)
        VALUES (%s,%s,%s,%s,%s)
    """, (order_id, row["product_id"], row["quantity"],
          row["unit_price"], row["quantity"] * row["unit_price"]))

conn.commit()

# -------------------- Data Quality Report --------------------
with open("data_quality_report.txt", "w") as f:
    for k, v in report.items():
        f.write(f"{k.upper()} DATA\n")
        for metric, value in v.items():
            f.write(f"{metric}: {value}\n")
        f.write("\n")

cursor.close()
conn.close()
logging.info("ETL Pipeline completed successfully")
