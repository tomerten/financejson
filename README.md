# FinanceJSON

FinanceJSON is a JSON based finance file format. JSON is able to describe complex 
data structures, 
has a human readable syntax and is available in all common programming languages. 
It is therefore an 
appropriate choice to store financial data in this format. Another advantage is 
that this format allows easy storage and data extraction.

## Specification
This repository contains the
[Specification of 
FinanceJSON](https://github.com/tomerten/financejson/blob/master/financejson/schema.json) 
in form of a [JSON Schema](https://json-schema.org). 

## Example

A FinanceJSON file for a stock:
```json
{
  "yh_symbol": "XYZ",
  "ms_symbol": "US_XYZ",
  "yh_currency": "USD",
  "ms_currency": "USD",
  "yh_esgScores": {
    "ratingyear": 2019,
    "ratingmonth": 9,
    "totalEsg": 12.4,
    "controversyOverview": [
      "alcohol",
      "nuclear"
    ]
  },
  "yh_earnings": {
    "earningsChart": {
      "quarterly": [
        {
          "date": "4Q2018"
        }
      ]
    },
    "financialChart": {
      "yearly": [
        {
          "date": "1Q2010"
        }
      ]
    }
  },
  "yh_indexTrend": {
    "estimates": [
      {
        "growth": 1,
        "period": "+1q"
      },
      {
        "growth": 1,
        "period": "-1q"
      },
      {
        "growth": 1,
        "period": "1q"
      },
      {
        "growth": 1,
        "period": "+1y"
      }
    ]
  }
}
```
 
 
# FinanceJSON CLI
[![Python 
Version](https://img.shields.io/pypi/pyversions/financejson)](https://pypi.org/project/financejson/)
[![PyPI](https://img.shields.io/pypi/v/financejson.svg)](https://pypi.org/project/financejson/)
[![CI](https://github.com/tomerten/financejson/workflows/CI/badge.svg)](https://github.com/tomerten/financejson/actions?query=workflow%3ACI)

This repository also contains a Python based commandline tool which is able 
validate and extract data from financeJSON files. It also emulate the linux ``tree``
command, printing out a tree structure of the JSON data.

Validate a financeJSON file:
```bash
financejson validate /path/to/financejsonfile
```

Print tree structure of financeJSON file:
```bash
financejson treejson /path/to/financejsonfile
```

Convert a financeJSON file into an HDF5 file:
```bash
financejson convert json hdf5 /path/to/financejsonfile
```

Convert a financeJSON file into an Excel readable file:
```bash
financejson convert json excel /path/to/financejsonfile
```
## License
[GNU General Public License 
v3.0](https://github.com/andreasfelix/latticejson/blob/master/LICENSE)


