from typing import List


class ArtistNotInDirectoryError(Exception):
    pass


class ArtistDirectory(object):
    """
    ADD ARTISTS HERE

    To find an artist's ID, visit https://open.spotify.com, search up an artist,
    and copy the ID that you see in the browser URL.

    Example:
        Browser URL: https://open.spotify.com/artist/4q3ewBCX7sLwd24euuV69X

        The ID is what comes after `/artist/`.
    """
    _artists = {
        "Drake": "3TVXtAsR1Inumwj472S9r4",
        "Beyonce": "6vWDO969PvNqNYHIOW5v0m",
        "Bad Bunny": "4q3ewBCX7sLwd24euuV69X",
        "Peso Pluma": "12GqGscKJx3aE4t07u7eVZ",
        "Coldplay": "4gzpq5DPGxSnKTe4SA8HAU",
        "Taylor Swift": "06HL4z0CvFAxyc27GXpf02",
        "Two Door Cinema Club": "536BYVgOnRky0xjsPT96zl",
        "Queen": "1dfeR4HaWDbWqFHLkxsg1d",
        "Michael Jackson": "3fMbdgg4jU18AjLCKBhRSm",
        "2Pac": "1ZwdS5xdxEREPySFridCfh",
        "J Cole": "6l3HvQ5sa6mXTsMTB19rO5",
    }
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def get_artist_id(self, name: str) -> str:
        artist_id = self._artists.get(name)

        if artist_id is None:
            raise ArtistNotInDirectoryError(
                f"Did not find artist named '{name}' in directory. "
                f"Look their ID up in Spotify and add them to the directory."
            )

        return artist_id

    def get_available_artists(self) -> List[str]:
        return list(self._artists)
