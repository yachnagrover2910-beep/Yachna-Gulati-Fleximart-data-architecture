Schema Documentation – Part 1 (ETL Pipeline – MySQL) 📌 Overview

This document describes the relational database schema used in Part 1 of the project. The schema is designed to store cleaned and standardized data after ETL processing from raw CSV files.

The database supports:

Customer master data

Product master data

Sales transactions

Referential integrity between entities

🗄️ Database: ecommerce_db 📋 Tables Overview Table Name Description customers Stores cleaned customer master data products Stores cleaned product master data sales Stores transactional sales data 1️⃣ Table: customers 📄 Description

Stores customer details after:

Deduplication

Phone number standardization

Date format normalization

Missing value handling

🧱 Table Structure Column Name Data Type Constraints Description customer_id VARCHAR(10) PRIMARY KEY Unique customer identifier first_name VARCHAR(50) NOT NULL Customer first name last_name VARCHAR(50) NOT NULL Customer last name email VARCHAR(100) NULL Customer email address phone VARCHAR(15) NOT NULL Standardized phone number city VARCHAR(50) NOT NULL Customer city (Title Case) registration_date DATE NOT NULL Customer registration date 🔑 Constraints

customer_id must be unique

email can be NULL

Phone numbers stored in numeric standardized format

Dates stored in YYYY-MM-DD

2️⃣ Table: products 📄 Description

Stores cleaned product data with standardized categories and validated pricing.

🧱 Table Structure Column Name Data Type Constraints Description product_id VARCHAR(10) PRIMARY KEY Unique product identifier product_name VARCHAR(100) NOT NULL Product name (trimmed) category VARCHAR(30) NOT NULL Normalized category price DECIMAL(10,2) NULL Product price stock_quantity INT NULL Available stock 🔑 Constraints

Categories normalized to:

Electronics

Fashion

Groceries

Price may be NULL for incomplete records

Stock may be NULL if unavailable

3️⃣ Table: sales 📄 Description

Stores transaction-level sales data after validation and cleansing.

🧱 Table Structure Column Name Data Type Constraints Description transaction_id VARCHAR(10) PRIMARY KEY Unique transaction ID customer_id VARCHAR(10) NULL Reference to customers product_id VARCHAR(10) NULL Reference to products quantity INT NOT NULL Quantity sold unit_price DECIMAL(10,2) NOT NULL Price per unit transaction_date DATE NOT NULL Transaction date status VARCHAR(20) NOT NULL Order status 🔗 Foreign Keys Column References customer_id customers(customer_id) product_id products(product_id)

Foreign keys allow NULLs to retain records with missing references for auditing.

🔐 Data Integrity Rules

Duplicate records removed during ETL

Date formats standardized to DATE

Orphan sales records retained but flagged

Referential integrity enforced where possible

Invalid or missing keys logged in data quality report

📈 Relationships Diagram (Logical) customers (1) ────< sales >──── (1) products

🧪 Example Queries Fetch Completed Sales with Customer Details SELECT s.transaction_id, c.first_name, c.last_name, s.transaction_date, s.quantity, s.unit_price FROM sales s JOIN customers c ON s.customer_id = c.customer_id WHERE s.status = 'Completed';