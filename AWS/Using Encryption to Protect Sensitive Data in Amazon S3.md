## Overview
Data protection refers to protecting data while in-transit as it travels to and from Amazon Simple Storage Service (Amazon S3) and at rest while it is stored on disks in Amazon S3 data centers. You can protect data in transit using Secure Socket Layer (SSL), Transport Layer Security (TLS), or client-side encryption. You have the following options for protecting data at rest in Amazon S3:
- Server-Side Encryption is when you request Amazon S3 to encrypt your objects before saving it on disks in its data centers and then decrypt it when you download the objects.
- Client-Side encryption is when you encrypt data on the client-side (locally) and upload the encrypted data to Amazon S3. In this case, you manage the encryption process, the encryption keys, and related tools.
## Conclusion
I have successfully:
- Explained the function of client-side and server-side encryption.
- Implemented default encryption on an S3 bucket
- Created an S3 bucket policy to enforce encryption in transit and at rest requirements.
