## Overview

 - Review user permissions in AWS IAM.
 - Capture audit evidence using AWS IAM Policy Simulator. You can use the IAM Policy Simulator to test the effects of AWS IAM policies to test your existing IAM policies to verify that they have the intended effect and capture the Policy Simulator output to use as support evidence in user access reviews.
 - Review Inbound and Outbound networking rules for Amazon EC2 Security Groups.
 - Review Amazon VPC configurations, subnets, and Network ACLs.
 - Review Amazon CloudWatch performance metrics.
 - Review raw Amazon CloudTrail logs within Amazon S3.


## What is a Security Group?

A security group acts as a virtual firewall for your instance to control inbound and outbound traffic. Security groups act at the instance level, not the subnet level. For each security group, you add rules that control the inbound traffic to instances and a separate set of rules that control the outbound traffic.


- You can specify allow rules, but not deny rules.
- You can specify separate rules for inbound and outbound traffic.
- By default, no inbound traffic is allowed until you add inbound rules to the security group.
- By default, all outbound traffic is allowed until you add outbound rules to the group. Then, you specify the outbound traffic that is allowed.
- Responses to allowed inbound traffic are allowed to flow outbound regardless of outbound rules and vice versa, as security groups are therefore stateful.
- Instances associated with a security group can’t talk to each other unless you add rules allowing it
- Exception: The default security group has these rules by default.
- After you launch an instance, you can change which security groups the instance is associated with.


## AWS CloudTrail

AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. With CloudTrail, you can log, continuously monitor, and retain account activity related to actions across your AWS infrastructure. CloudTrail provides event history of your AWS account activity, including actions taken through the AWS Management Console, AWS SDKs, command line tools, and other AWS services. This event history simplifies security analysis, resource change tracking, and troubleshooting.
