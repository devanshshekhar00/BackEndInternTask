# Google Calender
1) API Endpoint: auth.py
Description: This endpoint initiates the OAuth2 authentication flow with Google.
Method: POST
Request Payload: None
Response: Redirect URL for user authentication
2) API Endpoint: callback.py
Description: This endpoint handles the OAuth2 callback after successful user authentication.
Method: GET
Request Parameters: code (authorization code) and state (for verification)
Response: Access token and refresh token (optional)
3)API Endpoint: events.py
Description: This endpoint retrieves the events from the user's Google Calendar.
Method: GET
Request Parameters: None
Response: List of events
