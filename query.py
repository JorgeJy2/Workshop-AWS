import json
import boto3

client = boto3.client('dynamodb')

def handler(event, context):
  data = client.query(
    TableName='your-table-name',
    IndexName='some-index',
    KeyConditionExpression='#name = :value',
    ExpressionAttributeValues={
      ':value': {
        'S': 'shoes'
      }
    },
    ExpressionAttributeNames={
      '#name': 'name'
    }
  )

  response = {
      'statusCode': 200,
      'body': json.dumps(data),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }
  
  return response