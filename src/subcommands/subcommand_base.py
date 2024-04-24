import abc
import argparse

from src.api.spotify_api_client import SpotifyAPIClient
from src.artist_directory import ArtistDirectory


class SubcommandBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_name(self) -> str:
        raise NotImplementedError(f"Classes of type {type(self).__name__} must implement this method.")

    @abc.abstractmethod
    def add_subcommand_actions(self, subcommand_subparser_action) -> None:
        raise NotImplementedError(f"Classes of type {type(self).__name__} must implement this method.")

    @abc.abstractmethod
    def run(
            self,
            args: argparse.Namespace,
            spotify_api_client: SpotifyAPIClient,
            artist_directory: ArtistDirectory
    ) -> None:
        raise NotImplementedError(f"Classes of type {type(self).__name__} must implement this method.")
