from typing import List, Dict
import json
import pandas as pd

# write to excel
# writer = pd.ExcelWriter('results/results.xlsx', engine='xlsxwriter')
# cmp_df.to_excel(writer, sheet_name=cmp, index = False)

from .validate import validate_file


def convert_file(file_path, input_format, output_format):
    # validate file
    validate_file(file_path)

    # load json
    with open(file_path) as finance_file:
        finance_file = json.load(finance_file)

    # write to excel
    if input_format == 'json' and output_format == 'xlsx':
        writer = pd.ExcelWriter(
            # f'{file_path.split(".")[0]}.xlsx',
            'test.xlsx',
            engine='xlsxwriter'
        )

        for k, v in finance_file.items():
            if not isinstance(v, list):
                df = pd.DataFrame([{k: v}])
            else:
                df = pd.DataFrame(v)

            # excel sheet naming constraint
            if len(k) > 31:
                sheet_name = '_'.join(k.split('_')[-2:])
            else:
                sheet_name = k
            df.to_excel(writer, sheet_name=sheet_name, index=False)
        writer.save()

    # write to csv files
    elif input_format == 'json' and output_format == 'csv':
        for k, v in finance_file.items():
            if not isinstance(v, list):
                df = pd.DataFrame([{k: v}])
            else:
                df = pd.DataFrame(v)

            _filename = f'{file_path.split("/")[0]}'
            _filename += f'{k}.csv'
            df.to_csv(_filename, sep=',', index=False)

    # write to hdf5
    elif input_format == 'json' and output_format in ['h5', 'hdf', 'hdf5']:
        for k, v in finance_file.items():
            if not isinstance(v, list):
                df = pd.DataFrame([{k: v}])
            else:
                df = pd.DataFrame(v)

            name = f'{finance_file.get("yh_symbol", "")}'
            group = f'/{k}'
            df.to_hdf(f'{name}.h5',
                      key=group,  # internal path
                      mode='a',  # append mode - overwrites old file
                      format='table')  # table format

    else:
        raise NotImplementedError(f'Unknown formats: {input_format}, {output_format}')
