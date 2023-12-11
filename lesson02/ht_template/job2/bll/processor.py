import logging
import os
import json
import fastavro

from ht_template.job2.dal import local_disk

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

def process_raw_data(stg_dir: str, raw_dir: str) -> None:
    logging.info(f"Processing raw data from {raw_dir} to {stg_dir}...")
    for f in os.listdir(raw_dir):
        raw_file = os.path.join(raw_dir, f)
        logging.info(f'Processing file {raw_file}...')
        raw_data = json.load(open(raw_file, 'r'))
        local_disk.save_avro(
            raw_data, 
            path=os.path.join(
                stg_dir, 
                os.path.basename(raw_file).replace(".json", ".avro")))