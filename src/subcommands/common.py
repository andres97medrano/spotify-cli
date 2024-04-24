import argparse

from src.artist_directory import ArtistDirectory


def add_artist_argument(to_subparser: argparse.ArgumentParser):
    available_artists = ArtistDirectory().get_available_artists()

    to_subparser.add_argument(
        "artist",
        choices=available_artists,
        type=str,
        help=f"Artist name (select from: {', '.join(available_artists)}).",
        metavar="<artist>",
    )
