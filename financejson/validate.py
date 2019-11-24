import os
import json
import fastjsonschema

dir_name = os.path.dirname(__file__)
schema_path = os.path.join(dir_name, 'schema.json')

with open(schema_path) as schema_file:
    schema = json.load(schema_file)

validate = fastjsonschema.compile(schema)


def validate_file(file_path: str):
    with open(file_path) as finance_file:
        data = json.load(finance_file)

    validate(data)


def validate_dict(dc: dict):
        validate(dc)
