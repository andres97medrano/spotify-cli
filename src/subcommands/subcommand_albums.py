import argparse

from src.api.spotify_api_client import SpotifyAPIClient
from src.artist_directory import ArtistDirectory
from src.subcommands.common import add_artist_argument
from src.subcommands.subcommand_base import SubcommandBase


class AlbumsSubcommand(SubcommandBase):
    _name = "albums"

    def get_name(self) -> str:
        return self._name

    def add_subcommand_actions(self, subcommand_subparser_action) -> None:
        albums_subparser = subcommand_subparser_action.add_parser(
            name=self._name,
            help="Get album information about <artist>.",
        )
        add_artist_argument(to_subparser=albums_subparser)
        albums_subparser.add_argument(
            "-a",
            "--top-albums",
            type=int,
            required=False,
            default=10,
            help="Number of tops albums to get from <artist>.",
            metavar="<number>",
        )

    def run(
            self,
            args: argparse.Namespace,
            spotify_api_client: SpotifyAPIClient,
            artist_directory: ArtistDirectory
    ) -> None:
        artist = args.artist
        top_albums = args.top_albums

        artist_id = artist_directory.get_artist_id(name=artist)
        albums = spotify_api_client.get_artist_albums(artist_id=artist_id, top_albums=top_albums)

        indent = " " * 4
        print(f"Here are {artist}'s top albums:\n")

        for i, album in enumerate(albums):
            featured_artists = ", ".join([featured_artist.name for featured_artist in album.artists])
            print(f"{i + 1}. {album.name}")
            print(f"{indent}- Release Date: {album.release_date}")
            print(f"{indent}- Total Tracks: {album.total_tracks}")
            print(f"{indent}- Spotify Link: {album.link}")
            print(f"{indent}- Artist(s): {featured_artists}")
            print("\n")
