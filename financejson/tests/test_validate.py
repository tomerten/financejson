import os
import json
from financejson.validate import validate_file, validate_dict

dir_name = os.path.dirname(__file__)


def test_validate():
    file_path = os.path.join(dir_name, 'Data', 'yahoo_sustainability_test_data.json')
    validate_file(file_path)


def test_validate_dict():
    file_path = os.path.join(dir_name, 'Data', 'yahoo_sustainability_test_data.json')
    with open(file_path) as finance_file:
        dc = json.load(finance_file)
    validate_dict(dc)
