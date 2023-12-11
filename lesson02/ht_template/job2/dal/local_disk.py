import os
import logging
import fastavro

schema = {
    "doc": "Sales data reading.",
    "name": "Sales",
    "namespace": "sales",
    "type": "record",
    "fields": [
        {"name": "client", "type": "string"},
        {"name": "purchase_date", "type": {"type": "string", "logicalType": "date"}},
        {"name": "product", "type": "string"},
        {"name": "price", "type": "long"},
    ],
}


parsed_schema = fastavro.parse_schema(schema)


def save_avro(content: list[dict[str, any]], path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        logging.info(f"Writing Avro file {path}...")
        fastavro.writer(f, parsed_schema, content)