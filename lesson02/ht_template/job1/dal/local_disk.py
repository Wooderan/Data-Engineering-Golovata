import json
from typing import List, Dict, Any


def save_to_disk(json_content: List[Dict[str, Any]], path: str) -> None:
    # Check if json_content is a list of dictionaries
    if not (isinstance(json_content, list) and all(isinstance(item, dict) for item in json_content)):
        raise TypeError("json_content must be a list of dictionaries")

    with open(path, "w") as f:
        f.write(json.dumps(json_content))
