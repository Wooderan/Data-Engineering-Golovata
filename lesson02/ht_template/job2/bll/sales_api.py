import os.path
from pathlib import Path

from lesson02.ht_template.job2.dal import local_disk


def stage_sales_on_local_disk(raw_dir: str, stg_dir: str) -> None:
    Path(stg_dir).mkdir(parents=True, exist_ok=True)
    if not os.path.isdir(raw_dir):
        return
    for filename in os.listdir(raw_dir):
        source_file_path = os.path.join(raw_dir, filename)
        if os.path.isfile(source_file_path) and filename.endswith('.json'):
            data = local_disk.read_raw_from_disk(source_file_path)
            destination_file_path = os.path.join(stg_dir, filename.replace('.json', '.avro'))
            local_disk.save_stg_to_disk(data, destination_file_path)