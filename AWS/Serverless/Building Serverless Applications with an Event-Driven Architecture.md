## Overview

Serverless is the native architecture of the cloud. You can build serverless architectures for nearly any type of application or backend service—without thinking about servers. This type of architecture eliminates infrastructure management tasks such as server or cluster provisioning, patching, operating system maintenance, and capacity provisioning. Everything required to run and scale your application with high availability is handled for you.


## Objective
 - Understand an event-driven architecture
 - Understand how Step Functions is configured to orchestrate serverless applications
 - Take advantage of Amazon SQS and Amazon SNS
 - Create and configure Lambda functions and API Gateway resources
 - Made configuration updates to restore API functionality


In this lab, you build a web-based book printing app using a set of serverless technologies including Amazon API Gateway, AWS Step Functions, AWS Lambda, Amazon Simple Storage Service (Amazon S3), Amazon DynamoDB, Amazon Simple Notification Service (Amazon SNS), Amazon Simple Queue Service (Amazon SQS), and Amazon Rekognition.

This lab is built around a photo book printing application  
- user requests to generate presign urls for the album (collections), save urls to DynamoDB: API Gateway `/presigned` -> lambda PresignedUrlFunction -> save urls to DynamoDB table `imageMetadataTableName` -> return presigned urls
- user uploads to S3 a collection of images that they want printed in a physical book (send http request via command lines curl on Cloud9): API Gateway `presigned url` -> lambda function `???` saves image to S3 together with image meta data is saved to DynamoDB
- Trigger the Step Functions to manage the workflow by sending request to `/CreateBookBindingUrl`.  The user triggers the book creation process by indicating they have completed uploading images. This triggers the image-processing state machine.
- The workflow managed by state machin `ImageProcessStateMachine`, uses Lambda functions to make sure that each image is the proper file type (`ExtractImageMetadataFunc`, `TransformMetadataFunction`, `ImageValidationFunction`) and uses Amazon Rekognition to ensure that the content is appropriate. 
- lambdas `ResizeFunction`, `WatermarkFunction` resizes and watermarks the images and then generates a PDF proof for the customer to approve `ReadyForBookPrintFunction`, `DigitalBindingFunction`, `LambdaHumanApprovalSendE`. 
- Amazon SNS topic `xxxx-SNSTopicForUserCommunication-xxxx` sends an email to the customer for preview the PDF and approval before sending the job to Amazon SQS. 
- Amazon SQS queue `xxxx-BookPrintQueue-xxxx` sends off the book to the third-party printing service to be printed and shipped to the customer (`PrintVendorTrigger`, `BookprintStateMachine` -> `PrintVendorFunction`).

## Troubleshooting Serverless Applications

Unfortunately, the application was broken by a recent code push, and customers are receiving several errors as they attempt to provide images for their books. You will troubleshoot all of the issues and fix the application.

 - Enable and use AWS X-Ray and Amazon CloudWatch
 - Take advantage of Amazon Simple Queue Service (Amazon SQS) and dead-letter queues
 - Understand how to troubleshoot serverless architectures
 - Make configuration updates to restore API functionality

Api endpoints:
 - #0: `/batch` - This API Gateway is used for testing. It triggers a Lambda function that automates the user upload process contained in the orange box.
 - #1: `/addAlbum` - The user sends a request for presigned URLs to upload their images to. (it was `presigned` ?)
 - #2: The user uses the presigned URLs to upload their images directly to Amazon S3.
 - #3: `/CreateBookBinding` - The user triggers the book creation process by indicating they have completed uploading images.
 - #4: `/execution` - The PDF is approved by either the user acknowledging an email from Amazon SNS or by proxy using Lambda for testing.

### X-Ray

X-Ray generates trace maps that help identify the part of the application that is generating errors. X-Ray also stores detailed trace information, which can be used to troubleshoot issues.

By enabling for API Gateway, request that API gets under the four deployed API Gateway methods will inject the tracing header into the request. This will then flow to the Lambda function and allow you to see where a request is being dropped or hitting an error.


