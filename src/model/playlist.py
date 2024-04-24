import dataclasses
from typing import Dict, Any


@dataclasses.dataclass
class Playlist:
    name: str
    id: str
    link: str
    description: str

    def __init__(self, playlist_json: Dict[str, Any]):
        raise NotImplementedError("Implement this constructor.")
