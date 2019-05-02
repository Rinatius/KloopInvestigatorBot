import json

import constants as c
import strings as s
import snip
import search
from user import User
import sheets
from outgoing import message
from present import df_to_text

from botcommands import BotCommand


def lambda_handler(event, context):

    body = event[c.REQUEST_BODY]
    data = json.loads(body)
    query = data[c.REQUEST_QUERY]
    user_id = data[c.REQUEST_USER]

    response = snip.response200
    response[c.RESPONSE_BODY] = {}

    print("------Event from user received------")
    print(event)

    user = User(user_id)

    search.search(query, user)

    '''
    # EXAMPLE OF USING BOT COMMAND (instead of "search.search(query, user)")
    bot_command = BotCommand()
    bot_command.search(query, user)
    '''

    print("------RESULT------")
    print(user.current_result)

    if user.current_result is not None:

        if not user.current_result.empty:

            if user.status[c.USER_INTEGRATIONS][c.INTEGRATIONS_SHEETS] == c.INTEGRATION_STATUS_UNDECIDED:
                user.update_service_messages(s.sheets_undecided_service_message,
                                             [c.SHEETS_ON_BUTTON, c.SHEETS_OFF_BUTTON])

            #if user.status[c.USER_INTEGRATIONS][c.INTEGRATIONS_SHEETS]==c.INTEGRATION_STATUS_READY:
            #    user.service_messages[c.SERVICE_TEXTS].add(s.sheets_go_to_link_message + ' ' + user.status[sheet_link])

            if user.status[c.USER_INTEGRATIONS][c.INTEGRATIONS_SHEETS] == c.INTEGRATION_STATUS_READY:
                sheets.write(user)
        else:
            user.update_service_messages(s.no_results_message)

        #response[c.RESPONSE_BODY][c.RESPONSE_INFO] = df_to_text(user.current_result)

    #response[c.RESPONSE_BODY][c.RESPONSE_SERVICE_MESSAGES] = user.service_messages

    print(user.status)

    message(user)

    user.update()

    return response
