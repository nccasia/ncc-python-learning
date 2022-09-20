# Serverless 

*   [ ] You can create simple HTTP endpoint using API gateway
*   [ ] You know plugins to handle local development like serverless offline
*   [ ] Configure more robust triggers like SQS events
*   [ ] You know how to use WSGI based framework


Serverless is a deployment architecture where servers are not explicitly provisioned by the deployer. Code is instead executed based on developer-defined events that are triggered, for example when an HTTP POST request is sent to an API a new line written to a file.

## How can code be executed "without" servers?

Servers still exist to execute the code but they are abstracted away from the developer and handled by a compute platform such as Amazon Web Services Lambda or Google Cloud Functions.

Think about deploying code as a spectrum, where on one side you build your own server from components, hook it up to the internet with a static IP address, connect the IP address to DNS and start serving requests. The hardware, operating system, web server, WSGI server, etc are all completely controlled by you. On the opposite side of the spectrum are serverless compute platforms that take Python code and execute it without you ever touching hardware or even knowing what operating system it runs on.

## Serverless Offline

https://www.serverless.com/plugins/serverless-offline

