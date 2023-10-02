import json


class Response:
    @staticmethod
    def bad_exception_db_response(message, system_message=''):
        return {
            'statusCode': 503,
            'body': json.dumps({
                'message': message,
                'system_message': system_message
            })
        }

    @staticmethod
    def bad_response(message, code=500, system_message=''):
        return {
            'statusCode': code,
            'body': json.dumps({
                'message': message,
                'system_message': system_message
            })
        }

    @staticmethod
    def ok_response(data):
        return {
            'statusCode': 201,
            'body': json.dumps({
                'message': 'Product added.',
                'data': data
            }),
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            }
        }
