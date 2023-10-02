import re
from constant.regular_expresions import ID_REGULAR_EXPRESION


def check_params(body):
    if 'id' not in body:
        return 'Id param is required.'
    if not re.search(ID_REGULAR_EXPRESION, body['id']):
        return 'Bad format id.'
    return None
