
## SQL 
 
 - SQL is a query language to operate on sets. In detail **Structured Query Language** is a special-purpose programming language designed for managing data held in a relational database management system (RDBMS), or for stream processing in a relational data stream management system (RDSMS)

It is more or less standardized, and used by almost all relational database management systems: SQL Server, Oracle, MySQL, PostgreSQL, DB2, Informix, etc.

## SELECT

The result of a SELECT statement may be used as a value in another statement

```
SELECT name FROM world
  WHERE population >
     (SELECT population FROM world
      WHERE name='Russia')
```

### a correlated or synchronized sub-query

Find the largest country (by area) in each continent, show the continent, the name and the area

```
SELECT continent, name, area FROM world x
  WHERE area>= ALL
    (SELECT area FROM world y
        WHERE y.continent=x.continent
          AND area>0)
```

A correlated subquery works like a nested loop: the subquery only has access to rows related to a single record at a time in the outer query. The technique relies on table aliases to identify two different uses of the same table, one in the outer query and the other in the subquery.

### Operators over a set

These operators are binary - they normally take two parameters:
```
=     equals
>     greater than
<     less than
>=    greater or equal
<=    less or equal
```


You can use the words ALL or ANY where the right side of the operator might have multipl

```
SELECT name, continent, population FROM world x
  WHERE 25000000>=ALL (SELECT population FROM world y
                         WHERE x.continent=y.continent
                         AND population>0)
```

## Follow basic exercise here

https://sqlzoo.net/wiki/SQL_Tutorial


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







