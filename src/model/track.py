import dataclasses
from typing import List, Dict, Any

from src.model.album import Album
from src.model.artist import Artist


@dataclasses.dataclass
class Track:
    name: str
    id: str
    link: str
    popularity: int
    album: Album
    featured_artists: List[Artist]

    def __init__(self, track_json: Dict[str, Any]):
        self.name = track_json["name"]
        self.id = track_json["id"]
        self.link = track_json["external_urls"]["spotify"]
        self.popularity = track_json["popularity"]
        self.album = Album(album_json=track_json["album"])
        self.featured_artists = [
            Artist(artist_json=artist_json) for artist_json in track_json["artists"]
        ]
