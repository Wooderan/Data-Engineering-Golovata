import os
import shutil
from pathlib import Path

from lesson02.ht_template.job1.dal import local_disk, sales_api


def remove_directory_contents(path):
    """
    Removes all contents of the specified directory.

    Args:
    path (str): The path of the directory whose contents are to be removed.
    """
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')


def save_sales_to_local_disk(date: str, raw_dir: str) -> None:
    Path(raw_dir).mkdir(parents=True, exist_ok=True)
    remove_directory_contents(raw_dir)
    results = sales_api.get_sales(date)
    for i, result in enumerate(results):
        filename = f"sales_{date}_{i+1}.json"
        output_file = os.path.join(raw_dir, filename)
        local_disk.save_to_disk(result, output_file)

    return
