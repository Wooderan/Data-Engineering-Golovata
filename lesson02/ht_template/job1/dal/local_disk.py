import json
from typing import List, Dict, Any


def save_to_disk(json_content: List[Dict[str, Any]], path: str) -> None:
    with open(path, "w") as f:
        f.write(json.dumps(json_content))
