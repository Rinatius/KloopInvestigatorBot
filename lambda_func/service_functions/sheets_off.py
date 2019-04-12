import requests

import constants as c
import strings as s


def serve(user):

    # TODO Add check fo cases when this command is sent with integration off

    response = requests.post('https://accounts.google.com/o/oauth2/revoke',
                             params={'token': user.status[c.GOOGLE_OAUTH_CREDENTIALS].token},
                             headers={'content-type': 'application/x-www-form-urlencoded'})

    print("---------Response to /sheet_off------------")
    print(response)

    user.update_service_messages(s.integration_turned_off)

    user.status[c.GOOGLE_OAUTH_CREDENTIALS] = ''
    user.status[c.USER_INTEGRATIONS][c.INTEGRATIONS_SHEETS] = c.INTEGRATION_STATUS_REFUSED
    user.status[c.SPREADSHEET_ID] = ''
    user.status[c.SPREADSHEET_URL] = ''
