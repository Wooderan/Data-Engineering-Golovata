"""
This file contains the controller that accepts command via HTTP
and trigger business logic layer
"""
import os
import sys

from flask import Flask, request
from flask import typing as flask_typing

sys.path.append('/home/user/repos/DataEngineering.d/Data-Engineering-Golovata')
from lesson02.ht_template.job2.bll.sales_api import stage_sales_on_local_disk


app = Flask(__name__)


@app.route('/', methods=['POST'])
def main() -> flask_typing.ResponseReturnValue:
    """
    Controller that accepts command via HTTP and
    trigger business logic layer

    Proposed POST body in JSON:
    {
      "date: "2022-08-09",
      "raw_dir": "/path/to/my_dir/raw/sales/2022-08-09"
    }
    """
    input_data: dict = request.json
    raw_dir = input_data.get('raw_dir')
    stg_dir = input_data.get('stg_dir')

    if not raw_dir:
        return {
            "message": "raw_dir parameter missed",
        }, 400
    if not stg_dir:
        return {
            "message": "stg_dir parameter missed"
        }, 400

    stage_sales_on_local_disk(raw_dir=raw_dir, stg_dir=stg_dir)

    return {
               "message": "Data retrieved successfully from API",
           }, 201


if __name__ == "__main__":
    # app.run(debug=True, host="localhost", port=8081)
    app.run(port=8082)