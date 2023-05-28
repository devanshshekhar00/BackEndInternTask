from django.shortcuts import redirect
from google_auth_oauthlib.flow import Flow

def google_auth(request):
    # Define OAuth2 credentials and redirect URI
    client_id = 'YOUR_CLIENT_ID'
    client_secret = 'YOUR_CLIENT_SECRET'
    redirect_uri = 'YOUR_REDIRECT_URI'

    # Initialize OAuth2 flow
    flow = Flow.from_client_secrets_file(
        'credentials.json',
        scopes=['https://www.googleapis.com/auth/calendar'],
        redirect_uri=redirect_uri
    )

    # Generate authorization URL
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true'
    )

    # Store the state in session for later verification
    request.session['state'] = state

    # Redirect user to Google authentication page
    return redirect(authorization_url)
