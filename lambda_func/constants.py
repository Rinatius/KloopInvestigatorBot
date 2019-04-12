FIREBASE_SERVICE_ACCOUNT_JSON = "keys/alfa-bot-8d9cc-68b0eae3c6c5.json"
GOOGLE_INTEGRATIONS_REDIRECT_URI = "https://6vqfym8qgg.execute-api.us-east-1.amazonaws.com/default/gApiAuth"
GOOGLE_OAUTH_CLIENT_SECRET_FILE = "client_secret.json"

SHEETS_INTEGRATIONS_SCOPE = 'https://www.googleapis.com/auth/drive.file'

REQUEST_BODY = "body"
REQUEST_QUERY = "query"
REQUEST_USER = "user"
REQUEST_QUERY_STRING = "queryStringParameters"
REQUEST_QUERY_CODE = "code"
REQUEST_STATE = "state"

RESPONSE_BODY = "body"


RESPONSE_SERVICE_MESSAGES = "service_messages"
RESPONSE_INFO = "info"

LITERAL_SEARCH_SYMBOL = ":"
SERVICE_SYMBOL = "/"

DB_USERS_FIELD = "users"

USER_INTEGRATIONS = "integrations"
INTEGRATIONS_SHEETS = "sheets"
INTEGRATION_STATUS_UNDECIDED = "undecided"
INTEGRATION_STATUS_REFUSED = "refused"
INTEGRATION_STATUS_AGREED = "agreed"
INTEGRATION_STATUS_READY = "ready"
USER_STATUS_LAST_RESULT = "last_result"
USER_STATUS_LAST_QUERY = "last_query"
USER_STATUS_SALT = "salt"
USER_STATUS_SALT_TIME = "salt_time"

GOOGLE_OAUTH_CREDENTIALS = "google_oauth_credentials"


DEFAULT_USER_STATUS = {USER_INTEGRATIONS: {INTEGRATIONS_SHEETS: INTEGRATION_STATUS_UNDECIDED},
                       USER_STATUS_SALT: "",
                       GOOGLE_OAUTH_CREDENTIALS: "",
                       USER_STATUS_SALT_TIME: 0
                       }

SERVICE_BUTTONS = "service_buttons"
SERVICE_TEXTS = "service_texts"

SHEETS_ON_BUTTON = SERVICE_SYMBOL + "sheets_on"
SHEETS_OFF_BUTTON = SERVICE_SYMBOL + "sheets_off"

SALT_LIFE = 12000


SPREADSHEET_ID = "spreadsheet_id"


SPREADSHEET_CREATION_ATTEMPTS = 3


GENERATED_SHEET_NAME = "Bot generated sheet"


SPREADSHEET_URL = "spreadsheet_url"

MAX_SERVICE_MESSAGES = 4
MAX_BUTTONS_PER_SERVICE_MESSAGE = 4