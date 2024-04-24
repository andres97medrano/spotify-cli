import dataclasses
from typing import List, Dict, Any

from src.model.artist import Artist


@dataclasses.dataclass
class Album:
    name: str
    id: str
    release_date: str
    link: str
    total_tracks: int
    artists: List[Artist]

    def __init__(self, album_json: Dict[str, Any]):
        self.name = album_json["name"]
        self.id = album_json["id"]
        self.release_date = album_json["release_date"]
        self.link = album_json["external_urls"]["spotify"]
        self.total_tracks = album_json["total_tracks"]
        self.artists = [
            Artist(artist_json=artist_json) for artist_json in album_json["artists"]
        ]
