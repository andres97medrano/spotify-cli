"""
WARNING: DO NOT COMMIT ACTUAL SECRETS TO SOURCE

To get your CLIENT_ID and CLIENT_SECRET values, follow the guide at this link:
    https://developer.spotify.com/documentation/web-api/tutorials/getting-started

The relevant section has been copied below for convenience.

Create an app
    An app provides the Client ID and Client Secret needed to request an access token by implementing any of the
    authorization flows.

    To create an app, go to your Dashboard, click on the Create an app button and enter the following information:

        App Name: My App
        App Description: This is my first Spotify app
        Redirect URI: You won't need this parameter in this example, so let's use http://localhost:3000.

    Finally, check the Developer Terms of Service checkbox and tap on the Create button.
"""


class SpotifyCredentialsNotSetError(Exception):
    pass


def get_client_id() -> str:
    # return "YOUR_CLIENT_ID_HERE"
    raise SpotifyCredentialsNotSetError("Missing Spotify CLIENT_ID. Fill me in at credentials.py.")


def get_client_secret() -> str:
    # return "YOUR_CLIENT_SECRET_HERE"
    raise SpotifyCredentialsNotSetError("Missing Spotify CLIENT_SECRET. Fill me in at credentials.py.")
