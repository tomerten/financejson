from pytest import raises
import os
import json
from financejson.validate import validate_file, validate_dict
from fastjsonschema.exceptions import JsonSchemaException

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


def test_validate_real():
    file_path = os.path.join(dir_name, 'Data', 'test.json')
    validate_file(file_path)


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
        "yh_price_data_1d": [
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
        "yh_price_data_1d": [
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
        "yh_price_data_1d": [
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
        "yh_price_data_1d": [
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
        "yh_price_data_1d": [
            {
                "date": "01-01-2019 12:00:00.000T+0400",
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


def test_validate_dict___yh_price_data_1d___nok_wrong_field_type():
    dc = {
        "yh_symbol": "AAPL",
        "ms_symbol": "US_AAPL",
        "yh_price_data_1d": [
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

# def test_validate___yh_symbol_1(tmp_path):
#     data = {'yh_symbol' : 'AAPL'}
#     d = tmp_path / "sub"
#     d.mkdir()
#     p = d / "yh_symbol.json"
#     with open(p,'w') as f:
#         json.dump(data,f)
#     # p.write_text(data)
#     v
