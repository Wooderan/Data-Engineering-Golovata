import os
import json
from typing import List, Dict, Any


def save_to_disk(json_content: List[Dict[str, Any]], path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(json_content, f, indent=2)