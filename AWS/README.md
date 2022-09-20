## AWS

[Short description for reading](https://github.com/open-guides/og-aws)

Lab for practicing: https://amazon.qwiklabs.com/. Please take as many labs as posible. In each lab, there will be a student AWS account for you to login and do the exercise.

Apply for the free courses first(introductory labs), while trying to ask for free credits here
https://edu.google.com/programs/credits/training/?modal_active=none

We can also register the new account has 30-day trial in case you have a credit card. 

Create a branch with your name and add a report for each lab you finish, then push the branch and notify your supervisor. Each lab and report should be finished within 4 hours.

There is another way is registering for an AWS Free tie account and follow the following courses

## Setup local AWS CLI and credential

https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html

Note: if you do not have an AWS account, you can connect to the lab EC2 instance using provided PEM file in each lab -- not confirmed, please ignore this for now

Lab name:
 - AWS Tools for Windows PowerShell: Getting Started 
 - Automating AWS Services with Scripting and the AWS CLI (important)

## S3 and EC2

Lab name: 
 - Introduction to Amazon Simple Storage Service (S3) (free) - S3, EC2, bucket policy
 - Introduction to Amazon EC2 (free)
 - Introduction to Amazon Elastic Block Store (Amazon EBS) (free)
 - Managing Access to Amazon S3 Resources with Amazon VPC Endpoints 
 - Using Open Data with Amazon S3 
 - Using Encryption to Protect Sensitive Data in Amazon S3 


## IAM Identities (User, role, policy and permission)

https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html

Lab name:
 - Introduction to AWS Identity and Access Management (IAM) (free)

## RDS

Amazon Relational Database Service (Amazon RDS) makes it easy to set up, operate, and scale a relational database in the cloud. 

https://aws.amazon.com/rds/

Lab name
 - Introduction to Amazon Relational Database Service (RDS) (Linux)
 - Using Amazon RDS for Applications
 - Introduction to Amazon Aurora

## Serverless achitechture and Lambda function

Serverless architecture (also known as serverless computing or function as a service, FaaS) is a software design pattern where applications are hosted by a third-party service, eliminating the need for server software and hardware management by the developer.

AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers

Lab name:
 - Introduction to AWS Lambda (free)
 - Serverless Design with AWS Lambda
 - Building Serverless Applications with an Event-Driven Architecture (important 16h)
 - Troubleshooting Serverless Applications (advance)

AWS Lambda lets you run code without provisioning or managing servers. You pay only for the compute time you consume. With Lambda, you can run code for virtually any type of application or backend service—all with zero administration. Just upload your code, and Lambda takes care of everything required to run and scale your code with high availability. You can set up your code to automatically trigger from other AWS services or call it directly from any web or mobile app.

### Amazon Simple Queue Service

Amazon Simple Queue Service (Amazon SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. Amazon SQS eliminates the complexity and overhead associated with managing and operating message-oriented middleware and empowers developers to focus on differentiating work. Using Amazon SQS, you can send, store, and receive messages between software components at any volume, without losing messages or requiring other services to be available.

### Step functions

AWS Step Functions lets you coordinate multiple AWS services into serverless workflows so you can build and update apps quickly. Using Step Functions, you can design and run workflows that stitch together services, such as AWS Lambda, AWS Fargate, and Amazon SageMaker, into feature-rich applications.

## Api Gateway

Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. APIs act as the "front door" for applications to access data, business logic, or functionality from your backend services

Lab name
 - Introduction to Amazon API Gateway (free) (important)

## Cloudwatch - log service

Lab name:
 - Collecting and Analyzing Logs with Amazon CloudWatch Logs Insights
 - Building Search into your Applications with Amazon CloudSearch
 - Serverless Architectures using Amazon CloudWatch Events and Scheduled Events with AWS Lambda
 - Troubleshooting Serverless Applications
 - 

## Big data tools

Lab name
 - Introduction to Amazon Redshift (free)
 - Analyze Big Data with Hadoop
 - Optimize slow databases with Amazon Aurora
 - Using Tableau Desktop with Amazon Redshift
 - Serverless Architectures with Amazon DynamoDB and Amazon Kinesis Streams with AWS Lambda
 - Amazon DynamoDB Streams and TTL
 - Centralized Log Processing with Amazon Elasticsearch Service
 - Exploring Google Ngrams with Amazon EMR and Hive

Amazon EMR is a managed service that makes it fast, easy, and cost-effective to run Apache Hadoop and Spark to process vast amounts of data. Amazon EMR also supports powerful and proven Hadoop tools such as Presto, Hive, Pig, HBase, and more.

Apache Hadoop is an open-source software project that can be used to efficiently process large datasets. Instead of using one large computer to process and store the data, Hadoop uses clusters of commodity hardware to analyze massive data sets in parallel.

Apache Tez is a framework for creating a complex directed acyclic graph (DAG) of tasks for processing data. In some cases, it is used as an alternative to Hadoop MapReduce. For example, Pig and Hive workflows can run using Hadoop MapReduce or they can use Tez as an execution engine.

Hive  is an open-source data warehouse and analytic package that runs on top of a Hadoop cluster. Hive scripts use an SQL-like language called Hive QL (query language) that abstracts programming models and supports typical data warehouse interactions. Hive enables you to avoid the complexities of writing Tez jobs based on directed acyclic graphs (DAGs) or MapReduce programs in a lower level computer language, such as Java.

Pig is an open-source Apache library that runs on top of Hadoop. The library takes SQL-like commands written in a language called Pig Latin and converts those commands into Tez jobs based on directed acyclic graphs (DAGs) or MapReduce programs. You do not have to write complex code using a lower level computer language, such as Java.


## Glue 

 - Crawler
 - Workflow: trigger and job


## Amazon CloudFront

is a web service that speeds up distribution of static and dynamic web content, such as .html, .css, .php, and image files. CloudFront delivers content through a worldwide network of data centers called edge locations . When a user requests content through CloudFront, the user is routed to the edge location that provides the lowest latency (time delay), so that content is delivered with the best possible performance. If the content is already in the edge location with the lowest latency, CloudFront delivers it immediately. If the content is not in that edge location, CloudFront retrieves it from an Amazon S3 bucket or an HTTP server (for example, a web server) that you have identified as the source for the definitive version of your content.

## DynamoDB

Lab name:
 - Introduction to Amazon DynamoDB (free)
 - Serverless Web Apps using Amazon DynamoDB
 - Amazon DynamoDB: Building a Serverless Web Application (advance)
 - Amazon DynamoDB Scans, Queries, and Indexes
 - Amazon DynamoDB CRUD Activities Using the AWS CLI and SDK


## Networking, Services management and devops

Lab name:
 - Performing a Basic Audit of your AWS Environment (fundamental)
 - Getting Started with DevOps on AWS
 - Security on  (free)
 - Introduction to AWS Key Management Service (free)
 - Introduction to Amazon Virtual Private Cloud (VPC)
 - Compute & Networking
 - Building Your First Amazon Virtual Private Cloud (VPC)
 - Deployment & Management
 - Creating an Amazon Virtual Private Cloud (VPC) with AWS CloudFormation
 - SysAdmin on AWS for Windows
 - Working with Amazon Elastic Container Service


## Update: free labs

 - Introduction to AWS Identity and Access Management (IAM)
 - Introduction to AWS Key Management Service
 - Introduction to AWS Device Farm
 - Introduction to Amazon Simple Storage Service (S3)
 - Introduction to Amazon Elastic Block Store (Amazon EBS)
 - Introduction to Amazon Redshift
 - Introduction to Amazon DynamoDB
 - Introduction to Amazon CloudFront
 - Security on AWS
 - Troubleshooting connectivity using EC2 Serial Console