## Overview

In this lab, you will deploy a fully functional Hadoop cluster, ready to analyze log data in just a few minutes. You will start by launching an Amazon EMR cluster and then use a HiveQL script to process sample log data stored in an Amazon S3 bucket. 

HiveQL is a SQL-like scripting language for data warehousing and analysis. You can then use a similar setup to analyze your own log files.

 - Having sample log data stored in Amazon S3 (access logs data from a service on CloudFront)
 - Launch a fully functional Hadoop cluster using Amazon EMR to process the data
 - Define the schema and create a `Hive` table for the data
 - Reads the CloudFront log files from Amazon S3 and parses the files using the Regular Expression Serializer/Deserializer (RegEx SerDe).
 - Writes the parsed results to the cloudfront_logs Hive table
 - Submits a HiveQL query against the data to retrieve the total requests per operating system for a given time frame
 - Writes the query results to your Amazon S3 output bucket
 - Download and view the results on your computer
 - Connect to the Hive CLI and run HiveQL query script to view the results.

