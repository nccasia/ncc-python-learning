## Overview

<p>You started a small crowdsourcing platform and built a portfolio of mobile and web applications that enables consumers to produce content based on current events. Initially, you used a MySQL database running on an Amazon EC2 instance to underpin your applications. As business grew, you started looking for a more scalable solution to manage your database requirements and handle a few challenges you experienced while hosting the database. After analyzing the market offerings, you decided to use Amazon Aurora for your growing workloads.</p>

<p>During the development of the new application, you noticed poor performance when retrieving data from the Aurora database. You suspect the issue may be related to poor query design. You will use different tools in Amazon Aurora  to find the problematic queries and optimize the queries.</p>

<p>Amazon Aurora is a MySQL- and PostgreSQL-compatible relational database engine built for the cloud. Aurora is fully managed by Amazon Relational Database Service (Amazon RDS), which automates time-consuming administration tasks like hardware provisioning, database setup, patching, and backups. Aurora is built on a modern, purpose-built distributed storage system. All data is distributed in three different AWS Availability Zones, across hundreds of storage nodes, with two copies per zone. The Aurora MySQL- and PostgreSQL-compatible database engines are customized to take advantage of the fast distributed storage.</p>

<p>In this lab, you will use the IMDb dataset to test the Amazon RDS Aurora cluster. You will use slow query logs and Amazon RDS Performance Insights to evaluate your queries. Then you will fine-tune the query and evalute performance gains. You will also learn to configure auto scaling for read replicas in the Amazon Aurora cluster to mitigate peak load performance impacts. During this activity, you will review different parameters that are available to optimize the database performance for your workload.</p>

## Lab

 - IMDB dataset is store in a RDS cluster, including two database instances, reader and writer, are placed in different Availability Zones inside private subnets. 
 - Two Amazon EC2 instances are provisioned in a public subnet with access to the internet. One acts as `CommandHost` and other as a `traffic generator`. To access the database, you must first connect to the CommandHost, then connect to the database instances via port 3306. The environment also includes an Amazon CloudWatch dashboard with preconfigured widgets.</p>
 - Activate slow query logging in Aurora cluster: Modify parameter group to enable slow query logs, apply to the instance with the role Reader
 - Create CloudWatch Metrics for data visualization -> add slow log query into dashboard -> use CloudWatch dashboard to monitor DB performance
 - Check RDS Performance Insight: 
 - Query optimization -> use Explain to analyze the queries
 - Autoscaling
 - Generate trafic to trigger autoscaling

```
SELECT SQL_NO_CACHE DISTINCT
    name_display.name,
    name_facts.birthDate,
    name_facts.birthPLace,
    name_facts.deathPlace,
    name_facts.deathCause,
    name_facts.height,
    name_facts.gender
FROM
    name_facts
INNER JOIN title_cast ON name_facts.nameId = title_cast.nameId
INNER JOIN title_crew ON name_facts.nameId = title_crew.nameId
INNER JOIN name_display ON name_display.nameId = name_facts.nameId
WHERE
    name_display.name LIKE '%Matt Damon%';
```


```
SELECT SQL_NO_CACHE DISTINCT
    name_filmography.job,
    name_display.name,
    title_display.title,
    name_filmography.characters,
    title_cast.category
FROM
    title_display
INNER JOIN title_cast ON title_display.titleId = title_cast.titleId
INNER JOIN name_display ON title_cast.nameId = name_display.nameId
INNER JOIN title_genres ON title_genres.titleId = title_display.titleId
INNER JOIN name_facts ON name_facts.nameId = title_cast.nameId
INNER JOIN name_filmography ON title_display.titleId = name_filmography.titleId
WHERE
    name_display.name LIKE 'Tom Cruise'
LIMIT 100;
```

## Each row in the EXPLAIN contains the following fields:
<ul>
<li>
<strong>id</strong> – Represents a sequential number of the SELECT query that this row belongs to</li>
<li>
<strong>select_type</strong> – The type of SELECT query – in this case,  <em>SIMPLE</em>
</li>
<li>
<strong>table</strong> – The table name, or alias, that this row refers to</li>
<li>
<strong>type</strong> – Indicates how the tables are accessed/joined. The most popular access types you’ll see, from worst to best, are: ALL, index, range, ref, eq_ref, const, system</li>
<li>
<strong>possible_keys</strong> – Indicates the indexes from which MySQL can choose to find the rows in this table</li>
<li>
<strong>key</strong> – Indicates the actual index that MySQL decided to use</li>
<li>
<strong>key_len</strong> – Indicates the length of the key that MySQL decided to use. The value of key_len enables you to determine how many parts of a multiple-part key MySQL actually uses. If the key column says NULL, the len_len column also says NULL.</li>
<li>
<strong>rows</strong> – Indicates the number of rows MySQL believes it must examine to execute the query</li>
<li>
<strong>extra</strong> – Contains additional information about how MySQL resolves the query</li>
</ul>


## Autoscaling

To meet your connectivity and workload requirements, Aurora Auto Scaling dynamically adjusts the number of Aurora Replicas provisioned for an Aurora database cluster using single-master replication. Aurora Auto Scaling is available for both Aurora MySQL and Aurora PostgreSQL. Aurora Auto Scaling enables your Aurora database cluster to handle sudden increases in connectivity or workload. When the connectivity or workload decreases, Aurora Auto Scaling removes unnecessary Aurora Replicas so that you don't pay for unused provisioned database instances.

Run the python script to send mutiple requests to DB

```python
from __future__ import print_function # Python 2/3 compatibility
import pymysql
import time
import random
import multiprocessing


dbusername = 'dbadmin'
dbpassword = 'Pa33w0rd!'
dbhost = 'imdb-cluster.cluster-ro-cc0oh7xt3vay.us-west-2.rds.amazonaws.com'

DB_NAME = 'imdb'

sqlQuery1 = "SELECT COUNT(*) FROM ((((name_display JOIN title_cast) JOIN title_display) JOIN title_genres) JOIN name_facts) WHERE ((title_cast.nameId = name_display.nameId) AND (title_cast.titleId= title_display.titleId) AND (title_genres.titleId = title_display.titleId) AND (name_facts.nameId = title_cast.nameId)  AND (name_display.name = 'Sylvester Stallone') AND title_display.year = 1990)"

sqlQuery2 = "SELECT name_display.name FROM ((((name_display JOIN title_cast) JOIN title_display) JOIN title_genres) JOIN name_facts) WHERE ((title_cast.nameId = name_display.nameId) AND (title_cast.titleId= title_display.titleId) AND (title_genres.titleId = title_display.titleId) AND (name_facts.nameId = title_cast.nameId) AND (title_genres.genres like '%Sport') AND (title_display.year = 1990) AND title_display.runtimeMinutes > 90 )"



def queryTable():
    for i in range(1000000):
        conn = pymysql.connect(database="information_schema", user=dbusername, password=dbpassword, host=dbhost, port=3306, charset='utf8mb4')
        #print("Opened connections successfully")
        cur = conn.cursor()
        try:
            cur.execute("USE {}".format(DB_NAME))
            #print("Connected to Database {} successfully.".format(DB_NAME))
            cur.execute(sqlQuery1)

        except pymysql.Error as err:
            print("Database {} not found!!!.".format(DB_NAME))
        finally:
            conn.close()

import random
import multiprocessing
import time

if __name__ == "__main__":
    procs = 4   # Number of processes to create

    # Create a list of jobs and then iterate through
    # the number of processes appending each process to
    # the job list
    startTime = time.time()
    jobs = []
    for i in range(0, procs):
        process = multiprocessing.Process(target=queryTable)
        jobs.append(process)

    # Start the processes (i.e. calculate the random number lists)
    for j in jobs:
        j.start()

    # Ensure all of the processes have finished
    for j in jobs:
        j.join()

    print("List processing complete.")
    print ('The script took {0} second !'.format(round((time.time() - startTime),2)))

```
