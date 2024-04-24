import dataclasses
from typing import List, Optional, Dict, Any


@dataclasses.dataclass
class Artist:
    name: str
    id: str
    link: str
    popularity: Optional[int]
    followers: Optional[int]
    genres: Optional[List[str]]

    def __init__(self, artist_json: Dict[str, Any]):
        self.name = artist_json["name"]
        self.id = artist_json["id"]
        self.link = artist_json["external_urls"]["spotify"]
        self.popularity = artist_json.get("popularity")
        self.genres = artist_json.get("genres")
        self.followers = artist_json.get("followers", {}).get("total")
