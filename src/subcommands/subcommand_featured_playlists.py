import argparse

from src.api.spotify_api_client import SpotifyAPIClient
from src.artist_directory import ArtistDirectory
from src.subcommands.subcommand_base import SubcommandBase


class FeaturedPlaylistsSubcommand(SubcommandBase):
    _name = "featured-playlists"

    def get_name(self) -> str:
        return self._name

    def add_subcommand_actions(self, subcommand_subparser_action) -> None:
        featured_playlists_subparser = subcommand_subparser_action.add_parser(
            name=self._name,
            help="[NOT YET IMPLEMENTED] Fill me out.",
        )
        # TODO: Add an argument that allows the user to specify the top
        #       number of playlists they'd like to see.
        #
        #       See Python's argparse.ArgumentParser.add_argument documentation
        #       to find out what values are available to specify:
        #       https://docs.python.org/3.8/library/argparse.html#argparse.ArgumentParser.add_argument
        #
        #       You can also take a look at one of the previous subcommands that has added an argument
        #       (hint hint: see subcommand_albums.py).

        # featured_playlists_subparser.add_argument()

    def run(
            self,
            args: argparse.Namespace,
            spotify_api_client: SpotifyAPIClient,
            artist_directory: ArtistDirectory
    ) -> None:
        """
        STEP 1:
            You'll be using the featured playlists endpoint:
            https://developer.spotify.com/documentation/web-api/reference/get-featured-playlists

        STEP 2:
            Add a method to the `SpotifyAPIClient` class named `get_featured_playlists()`.

            Add a parameter to that method named `top_playlists: int` which represents how many of the top
            playlists you want to retrieve.

            The user should be able to specify this amount. You have access to that value through the `args` object.

            While testing out the method during implementation, you may want to print what the JSON response
            looks like so that you know how to parse it.

            That means inside your method, you can return the response as so:

                def get_featured_playlists(...):
                    ...
                    response = ...

                    return response

            and you can print it here as so:

                featured_playlists = spotify_api_client.get_featured_playlists()
                print(json.dumps(featured_playlists, indent=4))

                Note: You'll need to add an `import json` line to the top of the file.

            Once you've figured out the shape of the JSON and how you'd like to parse it, fill out
            the `Playlist` object inside of playlist.py.

        STEP 3:
            Call `spotify_api_client.get_featured_playlists()` method and display the information
            in any way you'd like.
        """

        print("ERROR: This subcommand has not yet been implemented. Fill me out.")
