import argparse

from src.api.spotify_api_client import SpotifyAPIClient
from src.artist_directory import ArtistDirectory
from src.subcommands.common import add_artist_argument
from src.subcommands.subcommand_base import SubcommandBase


class SimilarToSubcommand(SubcommandBase):
    _name = "similar-to"

    def get_name(self) -> str:
        return self._name

    def add_subcommand_actions(self, subcommand_subparser_action) -> None:
        songs_subparser = subcommand_subparser_action.add_parser(
            name=self._name,
            help="[NOT YET IMPLEMENTED] Get artists that are similar to <artist>.",
        )
        add_artist_argument(to_subparser=songs_subparser)

    def run(
            self,
            args: argparse.Namespace,
            spotify_api_client: SpotifyAPIClient,
            artist_directory: ArtistDirectory
    ) -> None:
        """
        STEP 1:
            Find out which API endpoint to use.
            Visit Spotify's API Docs: https://developer.spotify.com/documentation/web-api

        STEP 2:
            Implement the `get_similar_artists()` method in the `SpotifyAPIClient` class.
            Note which parameters you'll need from the user. You have access to the `args` and `artist_directory`
            objects in this method.

        STEP 3:
            Call `spotify_api_client.get_similar_artists()` method and display the information
            in any way you'd like.

        """
        print("ERROR: This subcommand has not yet been implemented. Fill me out.")
