from google.oauth2 import service_account
from googleapiclient.discovery import build

def get_events(request):
    # Load OAuth2 credentials
    credentials = service_account.Credentials.from_service_account_file(
        'credentials.json',
        scopes=['https://www.googleapis.com/auth/calendar']
    )

    # Build the Google Calendar API client
    service = build('calendar', 'v3', credentials=credentials)

    # Retrieve events from the user's calendar
    events_result = service.events().list(
        calendarId='primary',
        timeMin=datetime.datetime.utcnow().isoformat() + 'Z',
        maxResults=10,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])

    # Process and return the list
