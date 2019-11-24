from typing import List, Dict
import json
import pandas as pd

# write to excel
#writer = pd.ExcelWriter('results/results.xlsx', engine='xlsxwriter')
#cmp_df.to_excel(writer, sheet_name=cmp, index = False)

from .validate import validate


def convert_file(file_path, input_format, output_format):
    if input_format == 'json' and output_format == 'elegant':
        with open(file_path) as lattice_file:
            lattice_dict = json.load(lattice_file)

        validate(lattice_dict)
        return convert_json_to_elegant(lattice_dict)
    else:
        raise NotImplementedError(f'Unknown formats: {input_format}, {output_format}')
