from pytest import raises
import os
import json
import pandas as pd
from pandas.testing import assert_frame_equal
from financejson.validate import validate_file, validate_dict
from fastjsonschema.exceptions import JsonSchemaException
from financejson.convert import convert_file

dir_name = os.path.dirname(__file__)

currencies = [
    "AED",
    "ARS",
    "AUD",
    "BDT",
    "BGN",
    "BRL",
    "CAD",
    "CHF",
    "CNY",
    "COP",
    "CZK",
    "DKK",
    "EGP",
    "EUR",
    "GBP",
    "GEL",
    "GHS",
    "HKD",
    "HUF",
    "IDR",
    "ILS",
    "INR",
    "JMD",
    "JPY",
    "KRW",
    "KWD",
    "KZT",
    "MAD",
    "MXN",
    "MYR",
    "NGN",
    "NOK",
    "NZD",
    "OMR",
    "PEN",
    "PHP",
    "PKR",
    "PLN",
    "RON",
    "RUB",
    "SAR",
    "SEK",
    "SGD",
    "THB",
    "TRY",
    "TWD",
    "UAH",
    "USD",
    "VND",
    "ZAR"
]


def test_validate():
    file_path = os.path.join(dir_name, 'Data', 'yahoo_sustainability_test_data.json')
    validate_file(file_path)


# def test_validate_real():
#     file_path = os.path.join(dir_name, 'Data', 'test.json')
#     validate_file(file_path)


def test_validate_dict():
    file_path = os.path.join(dir_name, 'Data', 'yahoo_sustainability_test_data.json')
    with open(file_path) as finance_file:
        dc = json.load(finance_file)
    validate_dict(dc)


def test_validate_dict____yh_symbol():
    dc = {"yh_symbol": "AAPL"}
    with raises(JsonSchemaException):
        validate_dict(dc)


def test_validate_dict____ms_symbol():
    dc = {"ms_symbol": "US_AAPL"}
    with raises(JsonSchemaException):
        validate_dict(dc)


def test_validate_dict____yh_ms_symbol():
    dc = {
        "yh_symbol": "AAPL",
        "ms_symbol": "US_AAPL"
    }
    validate_dict(dc)


def test_validate_dict____yh_ms_symbol_integer_yh():
    dc = {
        "yh_symbol": 1,
        "ms_symbol": "US_AAPL"
    }
    with raises(JsonSchemaException):
        validate_dict(dc)


def test_validate_dict____yh_ms_symbol_integer_ms():
    dc = {
        "yh_symbol": "AAPL",
        "ms_symbol": 1
    }
    with raises(JsonSchemaException):
        validate_dict(dc)


def test_validate_dict____currency_ok(tmp_path):
    dc = {
        "yh_symbol": "AAPL",
        "ms_symbol": "US_AAPL"
    }
    for currency in currencies:
        dc["yh_currency"] = currency
        validate_dict(dc)


def test_validate_dict____currency_nok():
    dc = {
        "yh_symbol": "AAPL",
        "ms_symbol": "US_AAPL",
        "yh_currency": "BOE"
    }
    with raises(JsonSchemaException):
        validate_dict(dc)


def test_validate_dict____yh_price_data_1d_ok():
    dc = {
        "yh_symbol": "AAPL",
        "ms_symbol": "US_AAPL",
        "yh_ohlcv_1d": [
            {
                "date": "2019-01-01",
                "open": 1,
                "high": 2,
                "low": 3,
                "close": 4,
                "volume": 5
            }
        ]
    }
    validate_dict(dc)


def test_validate_dict____yh_price_data_1d___nok_missing_fields():
    dc = {
        "yh_symbol": "AAPL",
        "ms_symbol": "US_AAPL",
        "yh_ohlcv_1d": [
            {
                "open": 1,
                "high": 2,
                "low": 3,
                "close": 4,
            }
        ]
    }
    with raises(JsonSchemaException):
        validate_dict(dc)


def test_validate_dict___yh_price_data_1d___nok_wrong_date_format_1():
    dc = {
        "yh_symbol": "AAPL",
        "ms_symbol": "US_AAPL",
        "yh_ohlcv_1d": [
            {
                "date": "19-01-01",
                "open": 1,
                "high": 2,
                "low": 3,
                "close": 4,
                "volume": 5
            }
        ]
    }
    with raises(JsonSchemaException):
        validate_dict(dc)


def test_validate_dict___yh_price_data_1d___nok_wrong_date_format_2():
    dc = {
        "yh_symbol": "AAPL",
        "ms_symbol": "US_AAPL",
        "yh_ohlcv_1d": [
            {
                "date": "01-01-2019",
                "open": 1,
                "high": 2,
                "low": 3,
                "close": 4,
                "volume": 5
            }
        ]
    }
    with raises(JsonSchemaException):
        validate_dict(dc)


def test_validate_dict___yh_price_data_1d___nok_wrong_date_format_3():
    dc = {
        "yh_symbol": "AAPL",
        "ms_symbol": "US_AAPL",
        "yh_ohlcv_1d": [
            {
                "date": "2018-11-13T20:20:39+00:00",
                "open": 1,
                "high": 2,
                "low": 3,
                "close": 4,
                "volume": 5
            }
        ]
    }
    with raises(JsonSchemaException):
        validate_dict(dc)


def test_validate_dict___yh_price_data_1d___nok_wrong_field_type_open():
    dc = {
        "yh_symbol": "AAPL",
        "ms_symbol": "US_AAPL",
        "yh_ohlcv_1d": [
            {
                "date": "2019-01-01",
                "open": "boe",
                "high": 2,
                "low": 3,
                "close": 4,
                "volume": 5
            }
        ]
    }
    with raises(JsonSchemaException):
        validate_dict(dc)


def test_validate_dict___yh_price_data_1d___nok_wrong_field_type_high():
    dc = {
        "yh_symbol": "AAPL",
        "ms_symbol": "US_AAPL",
        "yh_ohlcv_1d": [
            {
                "date": "2019-01-01",
                "open": 1,
                "high": "boe",
                "low": 3,
                "close": 4,
                "volume": 5
            }
        ]
    }
    with raises(JsonSchemaException):
        validate_dict(dc)


def test_validate_dict___yh_price_data_1d___nok_wrong_field_type_low():
    dc = {
        "yh_symbol": "AAPL",
        "ms_symbol": "US_AAPL",
        "yh_ohlcv_1d": [
            {
                "date": "2019-01-01",
                "open": 1,
                "high": 2,
                "low": "boe",
                "close": 4,
                "volume": 5
            }
        ]
    }
    with raises(JsonSchemaException):
        validate_dict(dc)


def test_validate_dict___yh_price_data_1d___nok_wrong_field_type_close():
    dc = {
        "yh_symbol": "AAPL",
        "ms_symbol": "US_AAPL",
        "yh_ohlcv_1d": [
            {
                "date": "2019-01-01",
                "open": 1,
                "high": 2,
                "low": 3,
                "close": "boe",
                "volume": 5
            }
        ]
    }
    with raises(JsonSchemaException):
        validate_dict(dc)


def test_validate_dict___yh_price_data_1d___nok_wrong_field_type_volume():
    dc = {
        "yh_symbol": "AAPL",
        "ms_symbol": "US_AAPL",
        "yh_ohlcv_1d": [
            {
                "date": "2019-01-01",
                "open": 1,
                "high": 2,
                "low": 3,
                "close": 4,
                "volume": "1"
            }
        ]
    }
    with raises(JsonSchemaException):
        validate_dict(dc)


def test_validate_dict____yh_price_data_1m_ok():
    dc = {
        "yh_symbol": "AAPL",
        "ms_symbol": "US_AAPL",
        "yh_ohlcv_1m": [
            {
                "datetime": "2018-11-13T20:20:39+00:00",
                "open": 1,
                "high": 2,
                "low": 3,
                "close": 4,
                "volume": 5
            }
        ]
    }
    validate_dict(dc)


def test_validate_dict____yh_price_data_1m___nok_missing_fields():
    dc = {
        "yh_symbol": "AAPL",
        "ms_symbol": "US_AAPL",
        "yh_ohlcv_1m": [
            {
                "open": 1,
                "high": 2,
                "low": 3,
                "close": 4,
            }
        ]
    }
    with raises(JsonSchemaException):
        validate_dict(dc)


def test_validate_dict___yh_price_data_1m___nok_wrong_date_format_1():
    dc = {
        "yh_symbol": "AAPL",
        "ms_symbol": "US_AAPL",
        "yh_ohlcv_1m": [
            {
                "datetime": "13-11-2018T20:20:39+00:00",
                "open": 1,
                "high": 2,
                "low": 3,
                "close": 4,
                "volume": 5
            }
        ]
    }
    with raises(JsonSchemaException):
        validate_dict(dc)


def test_validate_dict___yh_price_data_1m___nok_wrong_field_type_open():
    dc = {
        "yh_symbol": "AAPL",
        "ms_symbol": "US_AAPL",
        "yh_ohlcv_1m": [
            {
                "datetime": "2018-11-13T20:20:39+00:00",
                "open": "boe",
                "high": 2,
                "low": 3,
                "close": 4,
                "volume": 5
            }
        ]
    }
    with raises(JsonSchemaException):
        validate_dict(dc)


def test_validate_dict___yh_price_data_1m___nok_wrong_field_type_high():
    dc = {
        "yh_symbol": "AAPL",
        "ms_symbol": "US_AAPL",
        "yh_ohlcv_1m": [
            {
                "datetime": "2018-11-13T20:20:39+00:00",
                "open": 1,
                "high": "2",
                "low": 3,
                "close": 4,
                "volume": 5
            }
        ]
    }
    with raises(JsonSchemaException):
        validate_dict(dc)


def test_validate_dict___yh_price_data_1m___nok_wrong_field_type_low():
    dc = {
        "yh_symbol": "AAPL",
        "ms_symbol": "US_AAPL",
        "yh_ohlcv_1m": [
            {
                "datetime": "2018-11-13T20:20:39+00:00",
                "open": 1,
                "high": 2,
                "low": "3",
                "close": 4,
                "volume": 5
            }
        ]
    }
    with raises(JsonSchemaException):
        validate_dict(dc)


def test_validate_dict___yh_price_data_1m___nok_wrong_field_type_close():
    dc = {
        "yh_symbol": "AAPL",
        "ms_symbol": "US_AAPL",
        "yh_ohlcv_1m": [
            {
                "datetime": "2018-11-13T20:20:39+00:00",
                "open": 1,
                "high": 2,
                "low": 3,
                "close": "4",
                "volume": 5
            }
        ]
    }
    with raises(JsonSchemaException):
        validate_dict(dc)


def test_validate_dict___yh_price_data_1m___nok_wrong_field_type_volume():
    dc = {
        "yh_symbol": "AAPL",
        "ms_symbol": "US_AAPL",
        "yh_ohlcv_1m": [
            {
                "datetime": "2018-11-13T20:20:39+00:00",
                "open": 1,
                "high": 2,
                "low": 3,
                "close": 4,
                "volume": "5"
            }
        ]
    }
    with raises(JsonSchemaException):
        validate_dict(dc)


def test_validate_dict___yh_assetprofile___ok():
    dc = {
        "yh_symbol": "AAPL",
        "ms_symbol": "US_AAPL",
        "yh_assetProfile": [
            {
                "date": "2019-01-01",
                "address1": "foo",
                "auditRisk": 1,
                "boardRisk": 2,
                "city": "bar",
                "country": "a"
            }],
        "yh_assetProfile_companyOfficers": [
            {
                "name": "boe",
                "title": "CEO"
            }
        ]
    }
    validate_dict(dc)


def test_validate_dict___yh_assetprofile___nok_missing_field_companyofficers():
    dc = {
        "yh_symbol": "AAPL",
        "ms_symbol": "US_AAPL",
        "yh_assetProfile": [
            {
                "date": "2019-01-01",
                "address1": "foo",
                "auditRisk": 1,
                "boardRisk": 2,
                "city": "bar",
                "country": "a"
            }],
        "yh_assetProfile_companyOfficers": [
            {
                "title": "CEO"
            }
        ]
    }
    with raises(JsonSchemaException):
        validate_dict(dc)


def test_convert_file___xlsx___ok():
    file_path = os.path.join(dir_name, 'Data', 'yahoo_sustainability_test_data.json')
    convert_file(file_path, 'json', 'xlsx')
    xls = pd.ExcelFile(f'test.xlsx')

    with open(file_path) as finance_file:
        finance_file = json.load(finance_file)

    _keys = [
        "yh_earnings_earningsChart_quarterly",
        "yh_earnings_financialsChart_yearly",
        "yh_assetProfile",
        "yh_assetProfile_companyOfficers",
        "yh_ohlcv_1d"
    ]

    for k in _keys:
        if len(k) > 31:
            sheet_name = '_'.join(k.split('_')[-2:])
        else:
            sheet_name = k
        df0 = pd.DataFrame(finance_file[k])
        df1 = pd.read_excel(xls, sheet_name)
        assert_frame_equal(df0, df1)

    _keys = [
        'yh_symbol',
        'ms_symbol'
    ]

    for k in _keys:
        if len(k) > 31:
            sheet_name = '_'.join(k.split('_')[-2:])
        else:
            sheet_name = k
        df0 = pd.DataFrame([{k: finance_file[k]}])
        df1 = pd.read_excel(xls, sheet_name)
        assert_frame_equal(df0, df1)

    # os.remove(f'test.xlsx')


def test_convert_file_h5___ok():
    file_path = os.path.join(dir_name, 'Data', 'yahoo_sustainability_test_data.json')

    with open(file_path) as finance_file:
        finance_file = json.load(finance_file)

    name = f'{finance_file.get("yh_symbol", "")}'
    name = f'{name}.h5'

    # remove previous version if exists
    if os.path.isfile(name):
        os.remove(name)

    # convert to h5
    convert_file(file_path, 'json', 'h5')

    _keys = [
        "yh_earnings_earningsChart_quarterly",
        "yh_earnings_financialsChart_yearly",
        "yh_assetProfile",
        "yh_assetProfile_companyOfficers",
        "yh_ohlcv_1d"
    ]

    for k in _keys:
        group = f'/{k}'
        df0 = pd.DataFrame(finance_file[k])
        df1 = pd.read_hdf(name, key=group)
        assert_frame_equal(df0, df1)

    os.remove(name)


def test_convert_file_csv___ok():
    file_path = os.path.join(dir_name, 'Data', 'yahoo_sustainability_test_data.json')

    with open(file_path) as finance_file:
        finance_file = json.load(finance_file)

    _keys = [
        "yh_earnings_earningsChart_quarterly",
        "yh_earnings_financialsChart_yearly",
        "yh_assetProfile",
        "yh_assetProfile_companyOfficers",
        "yh_ohlcv_1d"
    ]

    # convert to h5
    convert_file(file_path, 'json', 'csv')

    for k in _keys:
        df0 = pd.DataFrame(finance_file[k])
        _filename = f'{file_path.split("/")[0]}'
        _filename += f'{k}.csv'
        df1 = pd.read_csv(_filename)
        assert_frame_equal(df0, df1)

    # clean up files
    for k in finance_file.keys():
        _filename = f'{file_path.split("/")[0]}'
        _filename += f'{k}.csv'
        os.remove(_filename)
