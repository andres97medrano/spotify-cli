import argparse

from src.api.spotify_api_client import SpotifyAPIClient
from src.artist_directory import ArtistDirectory
from src.subcommands.common import add_artist_argument
from src.subcommands.subcommand_base import SubcommandBase


class SongsSubcommand(SubcommandBase):
    _name = "songs"

    def get_name(self) -> str:
        return self._name

    def add_subcommand_actions(self, subcommand_subparser_action) -> None:
        songs_subparser = subcommand_subparser_action.add_parser(
            name=self._name,
            help="Get song information about <artist>.",
        )
        add_artist_argument(to_subparser=songs_subparser)

    def run(
            self,
            args: argparse.Namespace,
            spotify_api_client: SpotifyAPIClient,
            artist_directory: ArtistDirectory
    ) -> None:
        artist = args.artist
        artist_id = artist_directory.get_artist_id(name=artist)
        tracks = spotify_api_client.get_artist_top_tracks(artist_id=artist_id)

        indent = " " * 4
        print(f"Here are {artist}'s top tracks:\n")

        for i, track in enumerate(tracks):
            featured_artists = ", ".join([featured_artist.name for featured_artist in track.album.artists])
            print(f"{i+1}. {track.name}")
            print(f"{indent}- Album: {track.album.name}")
            print(f"{indent}- Release Date: {track.album.release_date}")
            print(f"{indent}- Popularity: {track.popularity}")
            print(f"{indent}- Spotify Link: {track.link}")
            print(f"{indent}- Artist(s): {featured_artists}")
            print("\n")
