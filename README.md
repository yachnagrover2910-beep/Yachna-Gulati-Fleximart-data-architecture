Part 2 – NoSQL Product Catalog (MongoDB) 📌 Overview

Part 2 of this project focuses on designing and implementing a NoSQL data model using MongoDB to store a rich, semi-structured product catalog.

Unlike Part 1 (relational ETL in MySQL), this part demonstrates how MongoDB efficiently handles nested and hierarchical product data such as specifications, reviews, tags, and metadata.

🎯 Objectives

Design a document-based data model

Store complex product information in MongoDB

Leverage nested documents and arrays

Support flexible and scalable product catalog queries

📂 Input Dataset File Description products_catalog.json Product catalog with nested attributes and reviews 🧱 Data Model Design Collection: products_catalog

Each document represents one product and contains:

Product metadata

Nested specifications

Embedded customer reviews

Tags for search and filtering

Timestamps for auditing

📄 Document Structure { "product_id": "ELEC001", "name": "Samsung Galaxy S21 Ultra", "category": "Electronics", "subcategory": "Smartphones", "price": 79999.00, "stock": 150, "specifications": { }, "reviews": [ ], "tags": [ ], "warranty_months": 12, "created_at": "ISODate", "updated_at": "ISODate" }

🔍 Key Design Decisions ✅ Embedded Documents

Specifications and reviews are embedded for fast read performance

Avoids expensive joins required in relational databases

✅ Flexible Schema

Different products can have different specifications

Supports easy addition of new attributes without schema changes

✅ Read-Optimized Model

Optimized for product browsing, filtering, and analytics

Ideal for high-read e-commerce workloads

🛠️ Technologies Used

MongoDB

JSON

MongoDB Compass / Mongo Shell

Python (optional for loading)

▶️ How to Load Data Using Mongo Shell use ecommerce_db db.products_catalog.insertMany(require('./products_catalog.json'))

Using MongoDB Compass

Open MongoDB Compass

Select database: ecommerce_db

Select collection: products_catalog

Import products_catalog.json

🔎 Sample Queries Find All Electronics Products db.products_catalog.find( { category: "Electronics" }, { name: 1, price: 1, stock: 1 } )

Find Products with Rating ≥ 4 db.products_catalog.find({ "reviews.rating": { $gte: 4 } })

Find Products by Tag db.products_catalog.find({ tags: "smartphone" })

📈 Use Cases

Product browsing and search

Review analysis

Recommendation systems

Catalog analytics

🔮 Future Enhancements

Add indexing on category, price, and tags

Implement text search

Integrate with real-time recommendation engine

Add versioning for product updates

👤 Author

Yachna Gulati