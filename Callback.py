from django.shortcuts import redirect
from google_auth_oauthlib.flow import Flow

def google_auth_callback(request):
    # Verify the state parameter to prevent CSRF attacks
    state = request.GET.get('state', None)
    saved_state = request.session.get('state', None)

    if state is None or state != saved_state:
        # Handle invalid state
        return redirect('ERROR_PAGE')

    # Exchange authorization code for tokens
    client_id = 'YOUR_CLIENT_ID'
    client_secret = 'YOUR_CLIENT_SECRET'
    redirect_uri = 'YOUR_REDIRECT_URI'

    flow = Flow.from_client_secrets_file(
        'credentials.json',
        scopes=['https://www.googleapis.com/auth/calendar'],
        redirect_uri=redirect_uri
    )

    flow.fetch_token(
        authorization_response=request.build_absolute_uri(),
        client_id=client_id,
        client_secret=client_secret
    )

    # Store the access token and refresh token (optional)
    access_token = flow.credentials.token
    refresh_token = flow.credentials.refresh_token

    # Perform further actions with the access token and refresh token
    # For example, save them in the database for later use

    return redirect('SUCCESS_PAGE')
