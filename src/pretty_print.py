import json
from typing import Dict, Any


def pretty_print(json_obj: Dict[str, Any]) -> None:
    pretty_json_string = json.dumps(obj=json_obj, indent=4)

    print(pretty_json_string)


if __name__ == "__main__":
    example_json = {
        "school": "Oxnard College",
        "year_established": 1975,
        "mascot": "Condor",
        "address": {
            "street": "4000 S Rose Ave",
            "city": "Oxnard",
            "state": "California",
            "zip": 93033,
        }
    }

    pretty_print(example_json)
