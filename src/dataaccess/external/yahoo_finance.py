import requests
import json
import os

_HEADERS = {
        "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY"),
        "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

_STOCK_GET_SUMMARY = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary"
_STOCK_GET_HISTORICAL_DATA = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-historical-data" 


def get_stock_summary(symbol: setattr):
    params = {"symbol":symbol}
    response = requests.request("GET", _STOCK_GET_SUMMARY, headers=_HEADERS, params=params)
    return json.loads(response.text)


def get_stock_historical_data(symbol: str):
    params = {"symbol":symbol}
    response = requests.request("GET", _STOCK_GET_HISTORICAL_DATA, headers=_HEADERS, params=params)
    return json.loads(response.text)