import boto3

client = boto3.client('dynamodb')

def handler(event, context):
  data = client.put_item(
    TableName='indexador',
    Item={
        'user': {
           'S': 'demouser'
        },
        'id': {
          'S': '005'
        },
        'price': {
          'N': '500'
        },
        'name': {
          'S': 'Yeezys'
        }
    }
  )

  print(data)

  response = {
      'statusCode': 200,
      'body': 'successfully created item!',
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }
  
  return response



if __name__ == "__main__":
    handler(None, None)
    