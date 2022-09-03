## Overview

This lab shows how to create an Amazon Virtual Private Cloud (VPC) using AWS CloudFormation.

 - Deploy an AWS CloudFormation template that creates an Amazon VPC
 - Examine the components of the template
 - Update a CloudFormation stack
 - Examine a template with the AWS CloudFormation Designer
 - Delete a CloudFormation stack

## AWS CloudFormation

AWS CloudFormation gives developers and systems administrators an easy way to **create and manage a collection of related AWS resources, provisioning and updating** them in an orderly and predictable fashion.

### Template and stack

You can use AWS CloudFormation’s sample templates or create your own templates to describe the AWS resources, and any associated dependencies or runtime parameters, required to run your application. 

```
AWSTemplateFormatVersion: 2010-09-09
Description: Deploy a VPC

Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsHostnames: true
      Tags:
      - Key: Name
        Value: Lab VPC

  InternetGateway:
    Type: AWS::EC2::InternetGateway
    Properties:
      Tags:
      - Key: Name
        Value: Lab Internet Gateway

  AttachGateway:
    Type: AWS::EC2::VPCGatewayAttachment
    Properties:
      VpcId: !Ref VPC
      InternetGatewayId: !Ref InternetGateway

  PublicSubnet1:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: 10.0.0.0/24
      AvailabilityZone: !Select 
        - '0'
        - !GetAZs ''
      Tags:
        - Key: Name
          Value: Public Subnet 1

  PrivateSubnet1:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: 10.0.1.0/24
      AvailabilityZone: !Select 
        - '0'
        - !GetAZs ''
      Tags:
        - Key: Name
          Value: Private Subnet 1

  PublicRouteTable:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPC
      Tags:
        - Key: Name
          Value: Public Route Table

  PublicRoute:
    Type: AWS::EC2::Route
    Properties:
      RouteTableId: !Ref PublicRouteTable
      DestinationCidrBlock: 0.0.0.0/0
      GatewayId: !Ref InternetGateway

  PublicSubnetRouteTableAssociation1:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      SubnetId: !Ref PublicSubnet1
      RouteTableId: !Ref PublicRouteTable

  PrivateRouteTable:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPC
      Tags:
      - Key: Name
        Value: Private Route Table

  PrivateSubnetRouteTableAssociation1:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      SubnetId: !Ref PrivateSubnet1
      RouteTableId: !Ref PrivateRouteTable

Outputs:
  VPC:
    Description: VPC
    Value: !Ref VPC
  AZ1:
    Description: Availability Zone 1
    Value: !GetAtt 
      - PublicSubnet1
      - AvailabilityZone

```

You can deploy and update a template and its associated collection of resources (called a stack)

Once a CloudFormation stack has been deployed, it is recommended that any changes to the resources should be made through CloudFormation rather than by directly modifying the resources.

## Amazon Virtual Private Cloud (VPC)

lets you provision a logically isolated section of the AWS cloud where you can launch resources within a virtual network. 

You have complete control over your virtual networking environment, including selection of your own IP address range, creation of subnets, and configuration of route tables and network gateways.

## Internet Gateways

<p>An <strong>Internet gateway</strong> is a horizontally scaled, redundant, and highly available VPC component that allows communication between instances in your VPC and the Internet. It therefore imposes no availability risks or bandwidth constraints on your network traffic.</p>

An Internet gateway serves two purposes: to provide a target in your VPC route tables for Internet-routable traffic, and to perform network address translation (NAT) for instances that have been assigned public IPv4 addresses.

A VPC Gateway Attachment creates a relationship between a VPC and a gateway, such as this Internet Gateway.


