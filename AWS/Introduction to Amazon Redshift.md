
Amazon Redshift is a fast, fully managed  data warehouse that makes it simple and cost-effective to analyze all your data using standard SQL and your existing Business Intelligence (BI) tools.

Note: Athena is a serverless service and does not need any infrastructure to create, manage, or scale data sets. It works directly on top of Amazon S3 data sets. It creates external tables and therefore does not manipulate S3 data sources, working as a read-only service from an S3 perspective. 

Athena has an edge in terms of portability and cost, whereas Redshift stands tall in terms of performance and scale.

Amazon Athena charges for the amount of data scanned during query execution. $5 is charged for a TeraByte of data scanned. Scanned data is rounded off to the nearest 10 MB. There is no charge for DDL, Managing Partitions, and Failed Queries.

Pricing for Amazon Redshift depends on the cluster, ranging from $0.250 to $4.800 per hour for a DC instance, or $0.850 to $6.800 per hour for a DS instance.

- Launch a Redshift cluster
- Connect an SQL client to the Amazon Redshift cluster. In this task, you will use a web-based PostgreSQL client ("pgweb") to connect to Redshift.`http://35.161.32.176/`
- Load data from an S3 bucket into the Amazon Redshift cluster
- Run queries against data stored in Amazon Redshift

```
CREATE TABLE users (
  userid INTEGER NOT NULL,
  username CHAR(8),
  firstname VARCHAR(30),
  lastname VARCHAR(30),
  city VARCHAR(30),
  state CHAR(2),
  email VARCHAR(100),
  phone CHAR(14),
  likesports BOOLEAN,
  liketheatre BOOLEAN,
  likeconcerts BOOLEAN,
  likejazz BOOLEAN,
  likeclassical BOOLEAN,
  likeopera BOOLEAN,
  likerock BOOLEAN,
  likevegas BOOLEAN,
  likebroadway BOOLEAN,
  likemusicals BOOLEAN
);
```

```
COPY flights
FROM 's3://us-west-2-aws-training/awsu-spl/spl-17/4.2.9.prod/data/flights-usa'
IAM_ROLE 'INSERT-YOUR-REDSHIFT-ROLE'
GZIP
DELIMITER ','
REMOVEQUOTES
REGION 'us-west-2';
```

The data files are being loaded in parallel from Amazon S3. This is the most efficient way to load data into Amazon Redshift since the load process is distributed across multiple slices across all available nodes.

Each slice of a compute node is allocated a portion of the node's memory and disk space, where it processes a portion of the workload assigned to the node. The leader node manages distributing data to the slices and apportions the workload for any queries or other database operations to the slices. The slices then work in parallel to complete the operation.

When you create a table, you can optionally specify one column as the distribution key. When the table is loaded with data, the rows are distributed to the node slices according to the distribution key. Choosing a good distribution key enables Amazon Redshift to use parallel processing to load data and execute queries efficiently.

The CREATE TABLE command you ran earlier designated the carrier (airline) field as the Distribution Key (DISTKEY). This means the data will be split between the all available slices and nodes, but all data related to a particular carrier will always reside on the same slice. This improves processing speed when performing operations on the carrier field, such as GROUP BY and JOIN operations.

## Analyze Performance

You can use the EXPLAIN command to view how Amazon Redshift processes queries.

The plan shows the logical steps that Amazon Redshift will perform when running the query. Reading the Explain Plan from the bottom up, it displays a breakdown of logical operations needed to perform the query as well as an indication of their relative processing cost and the amount of data that needs to be processed. By analyzing the plan, you can often identify opportunities to improve query performance.

In traditional databases, a sequential scan (Seq Scan) across many rows of data can be very inefficient and is normally improved by adding an index. However, **Amazon Redshift does not use indexes**, yet is able to perform extremely fast queries across huge quantities of data – in this case, scanning over 96 million rows in a few seconds.

```
XN Limit (cost=1000156830987.88..1000156830987.90 rows=10 width=29)
 -> XN Merge (cost=1000156830987.88..1000156830988.84 rows=383 width=29)
  Merge Key: sum(flights.departures)
  -> XN Network (cost=1000156830987.88..1000156830988.84 rows=383 width=29)
    Send to leader
    -> XN Sort (cost=1000156830987.88..1000156830988.84 rows=383 width=29)
     Sort Key: sum(flights.departures)
     -> XN HashAggregate (cost=156830970.49..156830971.44 rows=383 width=29)
       -> XN Hash Join DS_BCAST_INNER (cost=4.79..156346841.73 rows=96825752 width=29)
        Hash Cond: ("outer".aircraft_code = "inner".aircraft_code)
        -> XN Seq Scan on flights (cost=0.00..968257.52 rows=96825752 width=11)
        -> XN Hash (cost=3.83..3.83 rows=383 width=32)
          -> XN Seq Scan on aircraft (cost=0.00..3.83 rows=383 width=32)
```

## Examining Disk Space and Data Distribution

Data in Amazon Redshift is distributed across multiple nodes and hard disks.

```
SELECT
  owner AS node,
  diskno,
  used,
  capacity,
  used/capacity::numeric * 100 as percent_used
FROM stv_partitions
WHERE host = node
ORDER BY 1, 2;
```

Run this query to see how much space is taken by each of the data tables:

```
SELECT
  name,
  count(*)
FROM stv_blocklist
JOIN (SELECT DISTINCT name, id as tbl from stv_tbl_perm) USING (tbl)
GROUP BY name;
```
## Amazon Redshift Primer

### Nodes Clusters

An Amazon Redshift data warehouse is a collection of computing resources called nodes. This collection of nodes is called a cluster. When you provision a cluster, you specify the type and the number of nodes that will make up the cluster. The node type determines the storage size, memory, CPU, and price of each node in the cluster:

### Scalability

If your storage and performance needs change after you initially provision your cluster, you can always scale the cluster in or out by adding or removing nodes, scale the cluster up or down by specifying a different node type, or you can do both. Resizing the cluster in either way involves minimal downtime. Resizing replaces the old cluster at the end of the resize operation. When you submit a resize request, the source cluster remains in read-only mode until the resize operation is complete.

### Parallel Processing

Amazon Redshift distributes workload to each node in a cluster and processes work in parallel, allowing processing speed to scale in addition to storage.

### Columnar Storage

Columnar storage for database tables is an important factor in optimizing analytic query performance because it drastically reduces the overall disk I/O requirements and reduces the amount of data you need to load from disk.

Rather than storing data values together for a whole row, Amazon Redshift stores data by column. This means that operations on a column require less disk I/O.

### Compression

Compression is a column-level operation that reduces the size of data when it is stored. Compression conserves storage space and reduces the size of data that is read from storage, which reduces the amount of disk I/O and therefore improves query performance.

### Snapshots as Backups

Snapshots are point-in-time backups of a cluster. You can create snapshots automatically or manually. Amazon Redshift stores these snapshots internally in Amazon S3 using an encrypted Secure Sockets Layer (SSL) connection. If you need to restore a cluster, Amazon Redshift creates a new cluster and imports data from the snapshot that you specify.

### Integrates With Existing Business Intelligence Tools

Amazon Redshift uses industry-standard SQL and is accessed using standard JDBC and ODBC drivers. Your existing Business Intelligence tools can easily integrate with Amazon Redshift.

