✅ nosql_analysis.md Section A: Limitations of RDBMS (≈150 words)

Relational databases work well when data structures are stable and uniform, but they struggle with highly diverse product catalogs. In FlexiMart’s case, different product types such as electronics, clothing, and furniture have completely different attributes. Modeling this in a relational database would require multiple nullable columns or separate tables, leading to sparse data and complex joins. Every time a new product type or attribute is introduced, the schema must be altered, which is costly and risky in production environments.

Additionally, storing customer reviews in a relational model requires separate tables and joins, making read operations slower and queries more complex. Nested data such as reviews, ratings, and specifications do not map naturally to rows and columns. As data volume grows, vertical scaling of RDBMS systems becomes expensive, limiting flexibility and performance for large-scale catalog expansion.

Section B: Benefits of MongoDB (≈150 words)

MongoDB addresses these limitations through its flexible, document-based schema. Each product can store only the attributes relevant to it, allowing laptops to include RAM and processor details while shoes include size and color without schema changes. This flexibility enables rapid onboarding of new product categories without database migrations.

MongoDB also supports embedded documents, making it ideal for storing customer reviews directly inside product documents. This improves read performance by eliminating joins and enables faster retrieval of complete product information. Additionally, MongoDB is designed for horizontal scalability through sharding, allowing FlexiMart to distribute large product catalogs across multiple nodes. This makes MongoDB highly suitable for dynamic, large-scale e-commerce environments where product variety and user-generated content continuously evolve.

Section C: Trade-offs (≈100 words)

One disadvantage of MongoDB is the lack of strong transactional guarantees compared to MySQL, especially for complex multi-document transactions. This can be a challenge for financial operations requiring strict consistency. Another drawback is data redundancy due to embedded documents, which can increase storage requirements and complicate updates when shared information changes. Therefore, MongoDB is best suited for flexible catalogs, while relational databases remain preferable for transactional systems like orders and payments.