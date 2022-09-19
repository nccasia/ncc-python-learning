## Overview

Use Amazon DynamoDB and a serverless AWS Lambda based architecture to deploy a web-based music application to complement its movie database application
 - It will allow users to show all music albums in the database, or those those of a certain genre.  
 - It will allow users to add or delete entries to the database, as well as update the non-key attributes of a given album.  
 - You have been tasked with creating and implementing this functionality combining Amazon DynamoDB, AWS Lambda, and Amazon API Gateway in conjunction with a front-end website you have been given.  
 - There is an optional task of integrating Amazon Cognito with the application to authorize users.

### Cognito

This service gives you the capability to manage authentication and aspects of authorization for your custom web and mobile applications through AWS

- It is a fully managed user directory service for custom applications.
- It also provides UI components from many platforms. So if you want to have a sign in or sign up UI, for example, for your iOS application or for your React web application of your Android application, you can get those out of the box with Cognito. 
- It also provides some advanced security controls to control account access.
- It also enables you to control access to AWS resources

## Lab

Use AWS CLI in Cloud 9

Upload (sync) static frontend files from a machine to S3 bucket

### Create a Dynamo table using a python script

```python


import boto3
import argparse

def create_new_dynamodb_table(namefortable):
  region=boto3.session.Session().region_name
  dynamodb = boto3.resource('dynamodb', region_name=region) #low-level client
  table = dynamodb.create_table(
    TableName=namefortable,
    KeySchema=[                                  # Specify the table keys
        {
            'AttributeName': 'Artist',
            'KeyType': 'HASH' #Partition Key
        },
        {
            'AttributeName': 'Album',
            'KeyType': 'RANGE' #Sort Key
        }
    ],
    AttributeDefinitions=[                      # Specify the other known table attributes
        {
            'AttributeName': 'Artist',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Album',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Genre',
            'AttributeType': 'S'
        }
    ],
    GlobalSecondaryIndexes=[                        #  Create the GSI on the Genre attribute
        {
            'IndexName': 'genre-index',
            'KeySchema': [
                {
                    'AttributeName': 'Genre',
                    'KeyType': 'HASH'
                },
            ],
            'Projection': {
                'ProjectionType': 'ALL',
            },
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 100,
                'WriteCapacityUnits': 100
            }
        }
    ],
    ProvisionedThroughput={                          # Set a high throughput value for the purposes of the lab
        'ReadCapacityUnits': 100,
        'WriteCapacityUnits': 100
    }
  )
  return table

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("tablename", help="name of the dynamodb table to create")    # Get the name of the table to create as a command line argument
    args = parser.parse_args()
    result = create_new_dynamodb_table(args.tablename)
    print("Table status:", result.table_status)
```

Show all Dynamo table 

```
aws dynamodb list-tables
```

Load data from a machine to Dynamo table using a python script

```python
import json
import argparse
import boto3
from pprint import pprint, pformat
import time
from decimal import Decimal

def load_dataset(dataset, targettable):

    region=boto3.session.Session().region_name
    dynamodb = boto3.resource('dynamodb', region_name=region) # low-level client
    table = dynamodb.Table(targettable)

    for dataitem in dataset:           # loop over each item in the dataset
        try:
            response = table.put_item(Item=dataitem)     # Use the put_item function to add each item to the table
        # handle error responses
        except ClientError as error:
            return error.response['Error']['Message']
        except Exception as error:
            print(error)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("tablename", help="name of the dynamodb table to target")   # Grab the name of the table and json file with data as command line arguments
    parser.add_argument("datafile", help="location of text data file, ex: movies.json")
    args = parser.parse_args()

    with open(args.datafile,"r") as json_file:
            data_list = json.load(json_file, parse_float=Decimal)     # take advantage of json.load class to ingest the data into a Python object
            load_dataset(data_list, args.tablename)  
            json_file.close()
```

### Create endpoints for CRUD

Read

```python
import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
import os
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    region=boto3.session.Session().region_name
    dynamodb = boto3.resource('dynamodb', region_name=region) #low-level Client
    table = dynamodb.Table(os.environ['tablename']) #define which dynamodb table to access

    if len(event['Genre']) > 0:
        try:
            totallist = table.query(                   # we want to use a query here for the most efficient data access
            IndexName="genre-index",                   # specify the name of the GSI created on the Genre attribute
            KeyConditionExpression = "Genre = :sortkeyval",     # Use a conditional expression with a placeholder to specify what key we want
            ExpressionAttributeValues = { ':sortkeyval' : event['Genre'] }  # give the actual value for the placeholder, which should equal the incoming event data
            )
        except ClientError as error:
            return error.response['Error']['Message']
        except BaseException as error:
            raise error
        return totallist['Items']
    else :
        try:
            scanreturn = table.scan()
            totallist = scanreturn['Items']

            while 'LastEvaluatedKey' in scanreturn.keys(): # if lastevaluatedkey is present, we need to keep scanning
                scanreturn = table.scan(
                    ExclusiveStartKey = scanreturn['LastEvaluatedKey']
                )
                totallist += scanreturn['Items']
            return totallist
        except ClientError as error:
            return error.response['Error']['Message']
        except Exception as error:
            print(error)
```


Add album

```python
import json
from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key, Attr
import time
from decimal import *
import os
from botocore.exceptions import ClientError

def lambda_handler(event,context):
    region=boto3.session.Session().region_name
    dynamodb = boto3.resource('dynamodb', region_name=region) #low-level Client
    table = dynamodb.Table(os.environ['tablename']) #define which dynamodb table to access

    try:
        response = table.put_item(     # since the Item is already in a json format as part of the incoming event object, we can pass it
            Item=event["Item"]             # directly to the put_item function 
        )
        return response
    # handle error responses
    except ClientError as error:
        return error.response['Error']['Message']
    except Exception as error:
        print(error)

```

Update album

```python
import json
import boto3
from decimal import Decimal
from botocore.exceptions import ClientError
import os

def lambda_handler(event, context):
    region=boto3.session.Session().region_name
    dynamodb = boto3.resource('dynamodb', region_name=region) #low-level Client
    table = dynamodb.Table(os.environ['tablename']) #define which dynamodb table to access

    try:
        response = table.update_item(                     # we want to use the update_item function here
            Key={
                'Artist': event["Item"]["Artist"],
                'Album': event["Item"]["Album"]
            },
            UpdateExpression="set Genre=:g, #R=:r, #Y=:y",     # We have to use placeholders for not only values, but attribute names since "Year" and "Rank" are reserved words
            ExpressionAttributeNames = { '#R' : "Rank", '#Y' : "Year" },  # specifying the actual attribute names
            ExpressionAttributeValues={                                   # linking the values for the attributes we want changed to the incoming event data
               ':r': Decimal(event["Item"]["Rank"]),
               ':g': event["Item"]["Genre"],
               ':y': event["Item"]["Year"]
            },
            ReturnValues="UPDATED_NEW"
        )
        return response['Attributes']
    # handle error responses
    except ClientError as error:
        return ClientError
    except Exception as error:
        print(error)

```


Delete album
```python
import json
from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key, Attr
import time
from decimal import *
from botocore.exceptions import ClientError
import os

def lambda_handler(event,context):
    region=boto3.session.Session().region_name
    dynamodb = boto3.resource('dynamodb', region_name=region) #low-level Client
    table = dynamodb.Table(os.environ['tablename']) #define which dynamodb table to access

    try:
        delstatus = table.delete_item(                    # perform delete
            Key={
                'Artist': event["Artist"],
                'Album': event["Album"]
            },
            ConditionExpression = "attribute_not_exists(#R) OR (#R > :min)",   # specifying the condition for deleting the item, with placeholders for actual names and values
            ExpressionAttributeNames = { '#R' : "Rank" },                      # providing the actual attribute name here, since rank is a reserved word in DynamoDB
            ExpressionAttributeValues={ ':min': 100 }                          # providing the numerical value here, since entering the number in the ConditionExpression would be read as a string
        )
        return delstatus
    except ClientError as error:
        return error.response['Error']['Message']
    except Exception as error:
        print(error)
```

### Config API Gateway

- create Rest API
- create resource `albums`
- create methods
- instruct the API to pass in a value from a query parameter to your Lambda function's event object. You will accomplish this with a mapping template
- enable cors