## Hadoop

Hadoop is a framework of the open source set of tools distributed under Apache License. It is used to manage data, store data, and process data for various big data applications running under clustered systems.

Components of Hadoop: Hadoop has three components: 

1. HDFS: Hadoop Distributed File System is a dedicated file system to store big data with a cluster of commodity hardware or cheaper hardware with streaming access pattern. It enables data to be stored at multiple nodes in the cluster which ensures data security and fault tolerance.
2. Map Reduce : Data once stored in the HDFS also needs to be processed upon. Now suppose a query is sent to process a data set in the HDFS. Now, Hadoop identifies where this data is stored, this is called Mapping. Now the query is broken into multiple parts and the results of all these multiple parts are combined and the overall result is sent back to the user. This is called reduce process. Thus while HDFS is used to store the data, Map Reduce is used to process the data.
3. YARN : YARN stands for Yet Another Resource Negotiator. It is a dedicated operating system for Hadoop which manages the resources of the cluster and also functions as a framework for job scheduling in Hadoop. The various types of scheduling are First Come First Serve, Fair Share Scheduler and Capacity Scheduler etc. The First Come First Serve scheduling is set by default in YARN.


## MR is a programming model

The MapReduce algorithm is a popular distributed algorithm. You can use it through the popular open source tool Apache Hadoop.

MapReduce in particular is built up from two simple ideas: the map function and the reduce function.

### The map function

 - Spread the work accross the machines
 - In the map phase input data, for instance a file, gets loaded and transformed into key-value pairs.
 - When each map phase is done it sends the created key-value pairs to the reducers where they are getting sorted by key.

### The reduce function

 - The idea is that you “reduce” a whole list of items down to one item. Collect and reduce works from machines.
 - Then the reduce phase is doing the computation of that key and its values and outputting the results.

MapReduce uses these two simple concepts to run queries about data across multiple machines. When you have a large dataset (billions of rows), MapReduce can give you an answer in minutes where a traditional database might take hours.

The problem with MapReduce is that there is no simple way to chain multiple map and reduce processes together. At the end of each reduce process the data must be stored somewhere.

This fact makes it very hard to do complicated analytics processes. You would need to chain MapReduce jobs together.

