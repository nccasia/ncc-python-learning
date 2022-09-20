# SQL 

Practice basic SQL syntax with Jupyter notebook. SQL is particularly useful in handling structured data where there are relations between different entities/variables of the data. SQL is a very important tool for data scientists to have in their repertoire.

In this tutorial, we will practice
1. How to create/connect a SQLite database
2. How to create a table from scratch/from an existing table
3. How to drop a table
4. How to insert data into/update a table
5. How to retrieve data
6. How to do maths across table columns
7. How to aggregate data
8. How to join tables
9. How to create/drop views to simplify queries
10. How to deal with NULLs
11. How to convert query results into Pandas's DataFrame
12. How to rollback and commit a transaction (this one used the sqlite3 package as ipython_sql does not support transactions).
13. (Bonus)How to access a SQLite database directly with Pandas
14. Dealing with date and time.

It is worth noting that this tutorial mainly focuses on how to retrieve data from a database, instead of database management. That is also why we slected SQLite rather than more complicated Databases such as MySQL or PostgreSQL, etc.

Moreover, this SQLite tutorial would not cover everything about SQLite. Some important features are left to be explored by users such as triger and transaction, primary or foreigh index, etc. 

The most efficient way to master SQL is to keep practicing through extensive hands-on practices. Hope that you could start using SQLite effectively and comfortably. 


## SQL 
 
 - SQL is a query language to operate on sets. In detail **Structured Query Language** is a special-purpose programming language designed for managing data held in a relational database management system (RDBMS), or for stream processing in a relational data stream management system (RDSMS)

It is more or less standardized, and used by almost all relational database management systems: SQL Server, Oracle, MySQL, PostgreSQL, DB2, Informix, etc.

## PostgresSQL

### Các kiểu dữ liệu và cấu trúc

Có một danh sách các kiểu dữ liệu PostgreSQL hỗ trợ. Bên cạnh kiểu số, floating-point, chuỗi, boolean, và các kiểu dữ liệu mà bạn mong muốn (và nhiều tùy chọn khác), PostgreSQL tự hào với uuid, tiền tệ, liệt kê (enumerated), hình học (geometric), nhị phân (binary), địa chỉ mạng, chuỗi bit, tìm kiếm văn bản, xml, json, mảng, hỗn hợp, và các loại khoảng (range types), cũng như một vài kiểu internal cho nhận biết đối tượng và vị trí đăng nhập. 

Để công bằng, MySQL, MariaDB và Firebird mỗi cái có một vài loại ở mức độ khác nhau, nhưng PostgreSQL hỗ trợ tất cả.


### Tạo một kiểu mới

Và nếu danh sách các loại dữ liệu mở rộng có sẵn của PostgreSQL là không đủ, bạn có thể sử dụng lệnh CREATE TYPE để tạo ra các kiểu dữ liệu mới như hỗn hợp (composite), liệt kê (enumerated), khoảng (range) và base. 


### Indexes

PostgreSQL provides several index types: **B-tree, Hash, GiST, SP-GiST, GIN and BRIN**. Each index type uses a different algorithm that is best suited to different types of queries. By default, the CREATE INDEX command creates B-tree indexes, which fit the most common situations.

### JSON

The best part of working with JSON in PostgreSQL is that you get to leverage all the normal SQL you already love along with these JSON functions. 

#### In the SELECT

```
The -> operator Returns JSON data in the form of a JSON key.
The ->> operator: Returns JSON data in the form of JSON text.

SELECT stud_data ->> 'name' AS StudentName FROM student;
```

```
The #> or #>> is the JSON path navigator with the difference being #> returns JSON and the #>> returns the JSON text value. 

SELECT json_content #> '{person, last_name}' FROM mytable;
```

#### In the Where clause

```
@> - operator looks for JSON that contains the JSON on the right side of the operator.

SELECT id, contacts from sites where contacts @> '{"city":"belfast"}'::jsonb 
```


#### functions

1. json_each - expand the outermost JSON object into a set of key-value pairs
2. json_object_keys - get a set of keys in the outermost JSON object
3. json_typeof - get the type of the outermost JSON value as a string

Advantages of using JSON in PostgreSQL are given below:

 - Avoid complicated joins.
 - Parsing of JSON data is quite easier and faster execution.
 - Compatible with various database management systems.
 - Javascript Notation Objects are faster and very easy to read and understand.
 - The data within the JSON object is separated by a comma which makes it easily understandable.
 - JSON is lightweight for data exchange.