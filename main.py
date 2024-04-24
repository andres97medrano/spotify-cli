import argparse
from typing import Dict

from src.api.spotify_api_client import SpotifyAPIClient
from src.artist_directory import ArtistDirectory
from src.credentials import get_client_id, get_client_secret
from src.subcommands.subcommand_albums import AlbumsSubcommand
from src.subcommands.subcommand_base import SubcommandBase
from src.subcommands.subcommand_similiar_to import SimilarToSubcommand
from src.subcommands.subcommand_songs import SongsSubcommand

if __name__ == "__main__":
    artist_directory = ArtistDirectory()
    available_artists = ", ".join(artist_directory.get_available_artists())

    parser = argparse.ArgumentParser(
        prog="Spotify Genie",
        description="Spotify Genie: Get information about your favorite artists, albums, and tracks from Spotify "
                    "plus more.",
        usage=argparse.SUPPRESS,
        epilog="Run `./spotify-genie <subcommand> -h` to learn more about a subcommand. Available artists in this "
               f"program are: {available_artists}. You can add more artists by updating artist_directory.py.",
    )

    # Add subparser to perform different actions
    subcommand_subparser_action = parser.add_subparsers(
        title="subcommands",
        dest="subcommand",
        metavar="[subcommand]",
    )
    subcommands = [
        SongsSubcommand(),
        AlbumsSubcommand(),
        SimilarToSubcommand(),
        # TODO: Challenge for the reader. Implement this subcommand.
        # FeaturedPlaylistsSubcommand(),
    ]
    subcommand_map: Dict[str, SubcommandBase] = {s.get_name(): s for s in subcommands}

    for subcommand in subcommands:
        subcommand.add_subcommand_actions(subcommand_subparser_action=subcommand_subparser_action)

    args = parser.parse_args()

    selected_subcommand = subcommand_map[args.subcommand]
    spotify_api_client = SpotifyAPIClient(client_id=get_client_id(), client_secret=get_client_secret())

    selected_subcommand.run(args=args, spotify_api_client=spotify_api_client, artist_directory=artist_directory)
