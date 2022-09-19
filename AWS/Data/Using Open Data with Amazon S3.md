## Overview
Amazon Simple Storage Service (Amazon S3) is safe, secure, highly scalable object storage in the cloud. It is commonly used for backup and storage, application or media hosting, high-traffic website hosting, or software delivery.

To get the most out of Amazon S3, you need to understand a few simple concepts:
- Amazon S3 stores data as objects within buckets. An object is composed of a file and, optionally, any metadata that describes that file.
- To store an object in Amazon S3, you upload it to a bucket. When you upload an object, you can set permissions on the object as well as any metadata.
- Buckets are the containers for objects. You can have one or more buckets. For each bucket, you can:
  - Control access to the bucket, defining who can create, delete, and list objects in the bucket.
  - View access logs for the bucket and its objects.
  - Choose the geographical region where Amazon S3 will store the bucket and its contents.
- You can create folders to group objects within buckets. You can also nest folders (create folders within folders). If you have used the Amazon S3 API or other utilities, you can learn some important aspects about how folders work with other grouping conventions in the [Amazon Simple Storage Service Console User Guide](http://docs.aws.amazon.com/AmazonS3/latest/UG/)

## Conclusion
I have successfully:
- Created an Amazon S3 bucket.
- Uploaded objects to Amazon S3.
- Set permissions on your bucket by creating a bucket policy.
- Created a CORS configuration policy for the bucket.
- Configured a bucket for static website hosting.
- Used JavaScript to display the contents of a bucket on a static webpage.
