## Overview
Amazon S3 supports Cross-Region Replication (CRR) for automatic, asynchronous copying of objects across buckets in different AWS Regions. Cross-Region Replication can help you:
- Comply with compliance requirements — Although Amazon S3 stores your data across multiple geographically distant Availability Zones by default, compliance requirements might dictate that you store data at even greater distances. Cross-region replication allows you to replicate data between distant AWS Regions to satisfy these requirements.
- Minimize latency — If your customers are in two geographic locations, you can minimize latency in accessing objects by maintaining object copies in AWS Regions that are geographically closer to your users.
- Increase operational efficiency — If you have compute clusters in two different AWS Regions that analyze the same set of objects, you might choose to maintain object copies in those Regions.
- Maintain object copies under different ownership — Regardless of who owns the source object you can tell Amazon S3 to change replica ownership to the AWS account that owns the destination bucket. This is referred to as the owner override option. You might use this option to restrict access to object replicas.
## Conclusion
 I have successfully:
 - Configured S3 buckets for versioning.
 - Created S3 Cross-Region Replication rules.
 - Replicated objects with rules for full buckets, encrypted files, folders, and tags.
 - Observed how the replication of deletions is handled.
 
