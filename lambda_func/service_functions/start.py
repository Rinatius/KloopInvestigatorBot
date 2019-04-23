import json
import constants as c
import snip
from outgoing import message
from user import User


def serve(user):

    greetings = 'Вас приветствует Бот бла бла бла ...!'
    user.update_service_messages(greetings)
    message(user)


def start_handler(event, context):

    body = event[c.REQUEST_BODY]
    data = json.loads(body)
    user_id = data[c.REQUEST_USER]

    response = snip.response200
    response[c.RESPONSE_BODY] = {}

    user = User(user_id)

    serve(user)