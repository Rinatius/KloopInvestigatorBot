import sys
sys.path.append('..')

import os
import crypt
import time
import json
import urllib

import google.oauth2.credentials
import google_auth_oauthlib.flow

import constants as c
import strings as s
    
def serve(user):
    
    print("--------Entered sheets_on function----------------")
    
    user.status[c.USER_STATUS_SALT] = crypt.mksalt(crypt.METHOD_SHA512)
    user.status[c.USER_STATUS_SALT_TIME] = time.time()
    user.status[c.USER_INTEGRATIONS][c.INTEGRATIONS_SHEETS] = c.INTEGRATION_STATUS_AGREED

    state = {'id': user.id, c.USER_STATUS_SALT: user.status[c.USER_STATUS_SALT]}
    state = json.dumps(state)
    #state = urllib.parse.quote_plus(state)
    
    # Use the client_secret.json file to identify the application requesting
    # authorization. The client ID (from that file) and access scopes are required.
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        'keys/'+c.GOOGLE_OAUTH_CLIENT_SECRET_FILE,
        scopes=[c.SHEETS_INTEGRATIONS_SCOPE])

    # Indicate where the API server will redirect the user after the user completes
    # the authorization flow. The redirect URI is required.
    flow.redirect_uri = c.GOOGLE_INTEGRATIONS_REDIRECT_URI

    # Generate URL for request to Google's OAuth 2.0 server.
    # Use kwargs to set optional request parameters.
    authorization_url, state = flow.authorization_url(
        # Enable offline access so that you can  an access token without
        # re-prompting the user for permission. Recommended for web server apps.
        access_type='offline',
        state=state,
        # Enable incremental authorization. Recommended as a best practice.
        include_granted_scopes='true')
    
    user.update_service_messages(s.click_auth_url + '\n' + authorization_url)

