import boto3
import os


def lambda_handler(event: any, context: any):

    user: str = event["user"]
    visit_count: int = 0

    # Prepare the DynamoDB client
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("indexador")
    print(table)
    response = table.get_item(Key={"user": "jorgeuser"})
    print(response)

   
    return response


if __name__ == "__main__":
    os.environ["TABLE_NAME"] = "indexador"
    test_event = {"user": "jorgeuser"}
    result = lambda_handler(test_event, None)
    print(result)