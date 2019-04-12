import io
import json

import google.oauth2.credentials
import pandas as pd

import adapter
import constants as c


class User:
    
    def __init__(self, user_id):
        self.id = user_id
        self.status = adapter.load_user_status(user_id)
        if self.status[c.GOOGLE_OAUTH_CREDENTIALS]:
            with open('keys/' + c.GOOGLE_OAUTH_CLIENT_SECRET_FILE) as f:
                secret = f.readline()
                secret = json.loads(secret)
                client_id = secret['web']['client_id']
                client_secret = secret['web']['client_secret']
            self.status[c.GOOGLE_OAUTH_CREDENTIALS] = google.oauth2.credentials.Credentials(
                client_id=client_id,
                client_secret=client_secret,
                **self.status[c.GOOGLE_OAUTH_CREDENTIALS])

        if (self.status.get(c.USER_STATUS_LAST_RESULT, None) is not None and
                self.status.get(c.USER_STATUS_LAST_RESULT, None) != ''):
            self.status[c.USER_STATUS_LAST_RESULT] = pd.read_csv(io.StringIO(self.status[c.USER_STATUS_LAST_RESULT]))
        self.service_messages = []
        self.current_result = None
        self.current_query = None
        
    def update(self):
        if self.status[c.GOOGLE_OAUTH_CREDENTIALS]:
            self.status[c.GOOGLE_OAUTH_CREDENTIALS] = self._credentials_to_dict(self.status[c.GOOGLE_OAUTH_CREDENTIALS])

        if self.current_result is not None:
            self.status[c.USER_STATUS_LAST_RESULT] = self.current_result.to_csv(index=False)
            self.status[c.USER_STATUS_LAST_QUERY] = self.current_query
        elif c.USER_STATUS_LAST_RESULT in self.status:
            self.status[c.USER_STATUS_LAST_RESULT] = self.status[c.USER_STATUS_LAST_RESULT].to_csv(index=False)

        adapter.update_user_status(self.id, self.status)

    def update_service_messages(self, text=None, buttons=None):
        self.service_messages.append({'text': text, 'buttons': buttons})

    def _credentials_to_dict(self, credentials):
        return {'token': credentials.token,
                'refresh_token': credentials.refresh_token,
                'token_uri': credentials.token_uri,
                'scopes': credentials.scopes}
