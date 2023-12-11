import os
from ht_template.job1.dal import local_disk, sales_api

def save_sales_to_local_disk(date: str, raw_dir: str) -> None:
    print("\tI'm in get_sales(...) function!")
    # 1. get data from the API
    data = sales_api.get_sales(date)
    # 2. save data to disk
    path = os.path.join(raw_dir, f"sales_{date}.json")
    local_disk.save_to_disk(data, path)    
