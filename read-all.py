import boto3
import os
import json


def lambda_handler(event: any, context: any):

    
    
    client = boto3.client('dynamodb')
    data = client.scan(
    TableName='indexador'
      )


   
    return json.dumps(data)


if __name__ == "__main__":
    os.environ["TABLE_NAME"] = "indexador"
    test_event = {"user": "jorgeuser"}
    result = lambda_handler(test_event, None)
    print(result)