import constants as c
import strings as s
import snip
from integrations import receive_credentials
from outgoing import message


def lambda_handler(event, context):
    query_string = event[c.REQUEST_QUERY_STRING]

    response = snip.response200
    response[c.RESPONSE_BODY] = {}

    if c.REQUEST_QUERY_CODE in query_string:
        response[c.RESPONSE_BODY][c.RESPONSE_SERVICE_MESSAGES] = receive_credentials(query_string)
    else:
        response = s.general_error

    return response
