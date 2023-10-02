# -*- encoding: utf-8 -*-
import json

import boto3
import os
from response import Response

from logger import Logger

from validators.payload import check_payload

LOCAL = True


def lambda_handler(event: any, context: any):

    logger = Logger.get_logger(LOCAL)
    logger.info(event)
    try:

        if 'body' not in event:
            logger.error('No params body sent')
            return Response.bad_response('No params body sent', 400)

        payload = json.loads(event['body'])
        
        message_error = check_payload(payload)
        if message_error is not None:
            logger.error(message_error)
            return Response.bad_response(message_error, 400)

        
        client = boto3.client('dynamodb')
        data = client.put_item(
            TableName='indexador',
            Item={
                'user': {
                'S': payload["name"]
                },
                'price': {
                'N': str(payload["price"])
                },
                'description': {
                'S': payload["description"]
                },
                'picture': {
                'S': payload["picture"]
                }
            }
        )
        print(data)

        return Response.ok_response(data)
   
    except Exception as error:
        logger.error('x Error unexpected : ' + str(type(error)) + ' ' + str(error))
        return Response.bad_response(str(error), 500)
    
    


if __name__ == "__main__":
    os.environ["TABLE_NAME"] = "indexador"
    test_event = {"user": "jorgeuser"}
    result = lambda_handler({
            "body": json.dumps({
                "name": "product name",
                "price": 7510.65,
                "description": "simple description",
                "picture": "http://www.google/product.png"
            })
        }, {})
    print(result)