import json
import urllib.error
import urllib.parse
import urllib.request
from typing import Dict, Any, Optional, List

from src.model.album import Album
from src.model.artist import Artist
from src.model.track import Track


class SpotifyAPIClient(object):
    def __init__(self, client_id: str, client_secret: str) -> None:
        self._client_id = client_id
        self._client_secret = client_secret
        self._access_token: Optional[str] = None

    def get_artist_top_tracks(self, artist_id: str) -> List[Track]:
        """
        Reference:
        https://developer.spotify.com/documentation/web-api/reference/get-an-artists-top-tracks
        """
        token = self._get_access_token()
        response = self._request(
            url=f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market=US",
            headers={
                "Authorization": f"Bearer {token}",
            }
        )

        return [
            Track(track_json=track_json) for track_json in response["tracks"]
        ]

    def get_artist_info(self, artist_id: str) -> Artist:
        """
        Reference:
        https://developer.spotify.com/documentation/web-api/reference/get-an-artist
        """
        token = self._get_access_token()
        response = self._request(
            url=f"https://api.spotify.com/v1/artists/{artist_id}",
            headers={
                "Authorization": f"Bearer {token}",
            }
        )

        return Artist(artist_json=response)

    def get_artist_albums(self, artist_id: str, top_albums: int) -> List[Album]:
        """
        Reference:
        https://developer.spotify.com/documentation/web-api/reference/get-an-artists-albums
        """
        token = self._get_access_token()
        response = self._request(
            url=f"https://api.spotify.com/v1/artists/{artist_id}/albums?limit={top_albums}",
            headers={
                "Authorization": f"Bearer {token}",
            }
        )

        return [Album(album_json=album_json) for album_json in response["items"]]

    # TODO: Add new methods below here...

    # =================================
    # PRIVATE METHODS
    # =================================
    def _get_access_token(self) -> str:
        if self._access_token:
            return self._access_token

        token_params = {
            "grant_type": "client_credentials",
            "client_id": self._client_id,
            "client_secret": self._client_secret,
        }
        auth_data = urllib.parse.urlencode(token_params).encode()
        response = self._request(
            url="https://accounts.spotify.com/api/token",
            encoded_data=auth_data,
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
            }
        )

        self._access_token = response["access_token"]

        return self._access_token

    @staticmethod
    def _request(url: str, headers: Dict[str, str], encoded_data: Optional[bytes] = None) -> Optional[Dict[str, Any]]:
        request = urllib.request.Request(url=url, data=encoded_data, headers=headers)

        with urllib.request.urlopen(url=request) as response:
            return json.loads(response.read().decode())
