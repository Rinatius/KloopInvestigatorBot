# First request to FlowXO that determines structure (limits) of all further requests

from user import User
import constants as c
from outgoing import message

dummy = 'dummy'
user = User(dummy)

for i in range(c.MAX_SERVICE_MESSAGES):
    user.update_service_messages(text=dummy, buttons=[dummy]*c.MAX_BUTTONS_PER_SERVICE_MESSAGE)

user.current_result = dummy

message(user)
