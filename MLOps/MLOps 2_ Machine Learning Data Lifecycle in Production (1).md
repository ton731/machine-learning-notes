# MLOps 2: Machine Learning Data Lifecycle in Production


###### tags: `MLOps`


### Data Journey

- **Data provenance (出處):**
    - 描述data的來源和background的資訊，包括data的原始來源、搜集方式、cleaning、transform步驟、儲存位置等。
    - 可以協助debugging
- **Data lineage (血統):**
    - 描述data如何被使用和轉化的概念。通常關注data從最開始到最終用途的轉換步驟，並追蹤這些路徑、目的和結果。
    - 對於資料需要遵守的規定極為重要，可以識別潛在的數據洩漏點、確保數據被適當使用，避免未授權的人使用並了解數據被用於哪些用途、監控數據存取和更改。
- **Data versioning:**
    - Code versioning: Github, ...
    - Environment versioning: Docker, Terraform, ...
    - Data versioning: DVC, Git-LFS, ...
- **Metadata:**
    - 在MLOps中，metadata指的是描述ML project各個component, dataset, model, expirement等資訊的屬性和特徵。
    - 如model detadata, data metadata, expirement metadata等

### Data Storage
ref: https://www.sap.com/taiwan/insights/what-is-a-data-warehouse.html

- **Feature Stores:**
    - 用來管理feature (ML model的input x)的中心化儲存庫，可以幫助ML Team有效管理、分享data feature。
    - 通常包括幾個主要功能：feature提取、存儲、管理、版本控制、服務化(轉成API service方便training和deployment調用)
    - 許多AI problem或是團隊可能要使用相同的feature，透過feature store，可以避免重複工作和data不一致的問題，並提高feature可重用性、可維護性。

- **Data Warehouse:**
    - ![](https://i.imgur.com/Vhdfolo.png)
    - ![](https://i.imgur.com/3YDGQGP.png)
    - Data warehouse是一個用來儲存、管理企業數據的集中式數據庫系統。主要目的是將從不同data source的data集中起來，通過一系列extract, transform, and load (ETL)過程轉換、清洗，而產生高質量的**structured data**，可以用於data analysis, buisness analysis。
    - Data warehouse屬於OLAP (online analytical processing)，目的並不是提供real-time的data，而是用於分析企業過去、現在等等的資料。

- **Data Lakes:**
    - ![](https://i.imgur.com/8N10E80.png)
    - Data lake為一種儲存大量**structured, unstructured raw data**的集中式儲存庫。優點是可以快速儲存和存取大量data。Data lake不用先定義資料格式，可以儲存各種資料格式。
    - Data lake通常會伴隨許多data transform和preprocessing。
    - 與data warehouse不同，data lake的儲存方式通常是在廉價的cloud上面，而data wareshouse則需要較貴的硬體軟體。因此data lake在處理大量unstructures data和需要real-time processing的場景下更為適合。
    - ![](https://i.imgur.com/Lvnz5IP.png)

- **Databases:**
    - Database主要是為了儲存structured data，例如交易紀錄、客戶資訊等，因此需要定義固定的資料格式(schema)，因此database能提供高度結構化的數據管理和**查詢**。

- Online analytical processing (OLAP) vs. Online transactional processing (OLTP)
    - ![](https://i.imgur.com/y41d7Vj.png)


### Advanced Data Labeling

- **Label propagation - Graph based:**
    - 藉由data間的community structure或是similarity來assign label給unlabeled data，把label從labeled data propagate到unlabeled data上。

- **Active Learning:**
    - 一些可以用來intelligently sampling data的algorithms。選擇一些對model training來說最informative的point來label。
    - 在constrained data budget, imbalanced dataset時會很helpful。
    - **Margin sampling:** 例如選擇在decision boundary最旁邊的那些margin unlabeled data，去label這些uncertain data可以幫助model performance。


### SQL vs. NoSQL
- **SQL Database(Structured Query Language):** 關聯式資料庫，將data存成表格，每個表格有固定的欄位和類型，且不同表格間可以建立關聯。SQL database用SQL語法來支援複雜的查詢和事務處理。例子：MySQL, PostgreSQL, Oracle。
- **NoSQL Database:** 非關聯式資料庫，通常不使用固定的表格結構，而用更靈活的方式存data，例如text, image等。NoSQL無法像SQL支援複雜的查詢，但提供高效的data讀寫，並可支持更大的系統。例子：MongoDB, Cassandra, Redis。


