## Overview 
Amazon Elastic Block Store (Amazon EBS) offers persistent storage for Amazon Elastic Compute Cloud (Amazon EC2) instances. EBS volumes are network-attached, and persist independently from the life of an instance. EBS volumes are highly available and are highly reliable volumes that can be leveraged as an EC2 instance boot partition or attached to a running EC2 instance as a standard block device.

When used as a boot partition, EC2 instances can be stopped and subsequently restarted enabling you to pay only for the provisioned storage resources while maintaining the instance's state. EBS volumes offer greatly improved durability over local EC2 instance stores because EBS volumes are automatically replicated within the Availability Zone to prevent data loss due to failure of a single piece of hardware.

For those wanting even more durability, Amazon EBS provides the ability to create point-in-time consistent snapshots of your volumes that are then stored in Amazon Simple Storage Service (Amazon S3) and automatically replicated across multiple Availability Zones. These snapshots can be used as the starting point for new EBS volumes and can protect your data for long-term durability. You can also easily share these snapshots with co-workers and other AWS developers.
## Conclusion
I have learned how to:
- Create an Amazon EBS volume.
- Attach an Amazon EBS volume to an Amazon EC2 instance.
- Create a file system on an Amazon EBS volume.
- Modify the size of an Amazon EBS volume. 
- Modify the volume type and performance characteristics of an Amazon EBS volume.
- Create snapshots for an Amazon EBS volume.
- Restore an Amazon EBS volume from a snapshot.
