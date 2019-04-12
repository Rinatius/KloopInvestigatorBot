from googleapiclient.discovery import build
from google.auth.exceptions import RefreshError
import pandas as pd

import constants as c
import strings as s


def create_spreadsheet(user):
    spreadsheet_service = build('sheets', 'v4', credentials=user.status[c.GOOGLE_OAUTH_CREDENTIALS])

    spreadsheet_body = {
        'sheets': [{'properties': {'gridProperties': {'columnCount': 26,
                                                      'rowCount': 1000},
                                   'index': 0,
                                   'sheetId': 0,
                                   'sheetType': 'GRID',
                                   'title': c.GENERATED_SHEET_NAME}}],
    }

    request = spreadsheet_service.spreadsheets().create(body=spreadsheet_body)
    response_create = request.execute()

    user.status[c.SPREADSHEET_ID] = response_create['spreadsheetId']
    user.status[c.SPREADSHEET_URL] = response_create['spreadsheetUrl']






def write(user, data=None):
    try:

        if not user.status.get(c.SPREADSHEET_ID):
            create_spreadsheet(user)

        spreadsheet_service = build('sheets', 'v4', credentials=user.status[c.GOOGLE_OAUTH_CREDENTIALS])

        #for i in range(c.SPREADSHEET_CREATION_ATTEMPTS):

        if data is None:
            data = user.current_result.to_csv(index=False)
        elif isinstance(data, pd.DataFrame):
            data = data.to_csv(index=False)

        grid_coordinate = {
            "sheetId": 0,
            "rowIndex": 0,
            "columnIndex": 0
        }

        api_requests = list()

        api_requests.append({
            "updateCells": {
                "range": {
                    "sheetId": 0
                },
                "fields": "userEnteredValue"
            }
        })

        api_requests.append({
            "pasteData": {
                "coordinate": grid_coordinate,
                "data": data,
                "type": "PASTE_VALUES",
                "delimiter": ","
            }
        })

        print("---------------Spreadsheet request----------------------")
        print(api_requests)

        body = {
            "requests": api_requests
        }

        response = spreadsheet_service.spreadsheets().batchUpdate(
            spreadsheetId=user.status[c.SPREADSHEET_ID],
            body=body).execute()


        print("------------Response after attempt to write a result to Google sheets-----------------")
        print(response)

        # TODO Finish logic regarding errors when writing to Google sheets
        user.update_service_messages(s.last_query_available_here + '\n' + user.status[c.SPREADSHEET_URL])
        # if response['preadsheetId'] == user.:
        #     user.update_service_messages(s.last_query_available_here + " " + user.status[c.SPREADSHEET_URL])
        # else:
        #     user.update_service_messages(s.something_wrong_writing_last_result)

    except RefreshError:
        user.update_service_messages(text=s.refresh_error_message, buttons=[c.SHEETS_OFF_BUTTON, c.SHEETS_ON_BUTTON])
