import re
from constant.regular_expresions import NAME_REGULAR_EXPRESION, AGE_REGULAR_EXPRESION, MESSAGE_REGULAR_EXPRESION, \
    TEXT_NUMBERS_SPACES_ACCENTS_POINTS


def check_payload(payload):
    if 'name' not in payload:
        return 'Name is required.'
    if not re.search(TEXT_NUMBERS_SPACES_ACCENTS_POINTS, payload['name']):
        return 'Bad format name.'
    if 'price' not in payload:
        return 'Price is required.'
    if type(payload['price']) != int and type(payload['price']) != float:
        return 'Bad format price.'
    if 'description' in payload:
        if not re.search(TEXT_NUMBERS_SPACES_ACCENTS_POINTS, payload['description']):
            return 'Bad format description.'
    if 'picture' in payload:
        if len(payload['picture']) <= 5:
            return 'Bad format picture.'
    if 'rating' in payload:
        if type(payload['rating']) != int and type(payload['rating']) != float:
            return 'Bad format rating.'
    return None
