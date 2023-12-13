import json
from typing import List, Dict, Any

from fastavro import parse_schema, writer

schema = {
        'doc': 'Client',
        'name': 'Client',
        'namespace': 'test',
        'type': 'record',
        'fields': [
            {'name': 'client', 'type': 'string'},
            {'name': 'purchase_date', 'type': 'string'},
            {'name': 'product', 'type': 'string'},
            {'name': 'price', 'type': 'int'},
        ]
    }
parsed_schema = parse_schema(schema)


def read_raw_from_disk(path: str) -> List[Dict[str, Any]]:
    with open(path, "r") as f:
        content = f.read()
        return json.loads(content)


def save_stg_to_disk(json_content: List[Dict[str, Any]], path: str) -> None:
    with open(path, 'wb') as f:
        writer(f, parsed_schema, json_content)