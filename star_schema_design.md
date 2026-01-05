Star Schema Design – Part 3 (Analytics & Reporting) 📌 Overview

This document describes the Star Schema design used in Part 3 of the project for analytical and reporting purposes.

The star schema is built on top of cleaned transactional data from Part 1 (MySQL) and enriched with product insights from Part 2 (MongoDB).

The design enables:

Fast analytical queries

Simplified joins

Business-friendly reporting

⭐ Why Star Schema?

Optimized for read-heavy analytics

Simple structure with fact and dimension tables

Easy to use in BI tools (Power BI, Tableau)

Improves query performance compared to normalized schemas

🏗️ Schema Overview dim_customer | | dim_date —— fact_sales —— dim_product | | dim_status

🧮 Fact Table 1️⃣ fact_sales 📄 Description

Stores transaction-level measurable metrics.

🧱 Structure Column Name Data Type Description sales_key INT Surrogate primary key transaction_id VARCHAR(10) Source transaction ID customer_key INT FK to dim_customer product_key INT FK to dim_product date_key INT FK to dim_date status_key INT FK to dim_status quantity INT Quantity sold unit_price DECIMAL(10,2) Price per unit total_amount DECIMAL(12,2) quantity × unit_price 📦 Dimension Tables 2️⃣ dim_customer 📄 Description

Stores customer descriptive attributes.

Column Name Data Type Description customer_key INT Surrogate primary key customer_id VARCHAR(10) Business key first_name VARCHAR(50) Customer first name last_name VARCHAR(50) Customer last name city VARCHAR(50) Customer city registration_date DATE Registration date 3️⃣ dim_product 📄 Description

Stores product attributes enriched with catalog data.

Column Name Data Type Description product_key INT Surrogate primary key product_id VARCHAR(10) Business key product_name VARCHAR(100) Product name category VARCHAR(30) Product category subcategory VARCHAR(50) Product subcategory price DECIMAL(10,2) Product price warranty_months INT Warranty period

Data can be enriched from MongoDB catalog where applicable.

4️⃣ dim_date 📄 Description

Stores date attributes for time-based analysis.

Column Name Data Type Description date_key INT YYYYMMDD full_date DATE Calendar date day INT Day of month month INT Month number month_name VARCHAR(15) Month name quarter INT Quarter year INT Year weekday VARCHAR(10) Weekday name 5️⃣ dim_status 📄 Description

Stores order status values.

Column Name Data Type Description status_key INT Surrogate primary key status VARCHAR(20) Order status (Completed, Pending, Cancelled) 🔗 Relationships

fact_sales.customer_key → dim_customer.customer_key

fact_sales.product_key → dim_product.product_key

fact_sales.date_key → dim_date.date_key

fact_sales.status_key → dim_status.status_key

📈 Example Analytical Queries Total Revenue by Category SELECT p.category, SUM(f.total_amount) AS revenue FROM fact_sales f JOIN dim_product p ON f.product_key = p.product_key GROUP BY p.category;

Monthly Sales Trend SELECT d.year, d.month_name, SUM(f.total_amount) AS monthly_revenue FROM fact_sales f JOIN dim_date d ON f.date_key = d.date_key GROUP BY d.year, d.month_name ORDER BY d.year, d.month;

🧠 Design Considerations

Surrogate keys used for performance

Slowly Changing Dimensions (Type 1) assumed

Fact table contains only numeric measures

Dimensions contain descriptive attributes

🔮 Future Enhancements

Implement SCD Type 2 for customers and products

Add dim_city or dim_location

Add promotional or campaign dimension

Build materialized views for BI tools

✅ Part 3 Deliverables

Star schema design

Analytical SQL queries

Business-ready reporting model

👤 Author

Yachna Gulati