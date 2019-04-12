import time
import json

import google_auth_oauthlib.flow
from urllib.parse import urlencode
import pandas as pd

import sheets
import strings as s
import constants as c
import outgoing
from user import User


def receive_credentials(query_string_params):
    print("------Integration request received------")
    print(query_string_params)

    # try:
    state = query_string_params[c.REQUEST_STATE]
    # state = unquote(state)

    authorization_response = c.GOOGLE_INTEGRATIONS_REDIRECT_URI + '?' + urlencode(query_string_params)
    print("----------------Auth response-----------------")
    print(authorization_response)

    state = json.loads(state)

    print('-----------State from request-----------------')
    print(state)

    user = User(state["id"])

    print('-----------Status from user-----------------')
    print(user.status)

    if (user.status[c.USER_STATUS_SALT] != "" and
            user.status[c.USER_STATUS_SALT] == state[c.USER_STATUS_SALT] and
            (time.time() - user.status[c.USER_STATUS_SALT_TIME]) < c.SALT_LIFE):
        # Use the client_secret.json file to identify the application requesting
        # authorization. The client ID (from that file) and access scopes are required.
        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
            'keys/' + c.GOOGLE_OAUTH_CLIENT_SECRET_FILE,
            scopes=[c.SHEETS_INTEGRATIONS_SCOPE])
        # Indicate where the API server will redirect the user after the user completes
        # the authorization flow. The redirect URI is required.
        flow.redirect_uri = c.GOOGLE_INTEGRATIONS_REDIRECT_URI
        flow.fetch_token(authorization_response=authorization_response)
        user.status[c.GOOGLE_OAUTH_CREDENTIALS] = flow.credentials
        print("-------Google credentials--------")
        print(flow.credentials)
        user.update_service_messages(s.integration_successfull)

        if c.USER_STATUS_LAST_RESULT in user.status and \
           isinstance(user.status[c.USER_STATUS_LAST_RESULT], pd.DataFrame):
            sheets.write(user, user.status[c.USER_STATUS_LAST_RESULT])

        user.status[c.USER_INTEGRATIONS][c.INTEGRATIONS_SHEETS] = c.INTEGRATION_STATUS_READY
        user.status[c.USER_STATUS_SALT] = ""

        user.update()
        outgoing.message(user)
        response = user.service_messages
    else:  # Be careful here! This else can be caused by an attempt of unauthorized access!!!
        response = s.something_went_wrong_with_sheets_integration

    return response
