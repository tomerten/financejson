import os
from financejson.validate import validate_file

dir_name = os.path.dirname(__file__)


def test_validate():
    print(dir_name)
    file_path = os.path.join(dir_name, 'Data', 'yahoo_sustainability_test_data.json')
    validate_file(file_path)