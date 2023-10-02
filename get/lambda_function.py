# -*- encoding: utf-8 -*-
import json

import boto3
import os
from response import Response

from logger import Logger

LOCAL = True


def lambda_handler(event: any, context: any):

    logger = Logger.get_logger(LOCAL)
    logger.info(event)
    try:
        client = boto3.client('dynamodb')
        data = client.scan(TableName='indexador')
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