
BASE_URL = "https://www.alphavantage.co/query?"
API_KEY = "QEQT8WNAUX7DRILI"

INTERVAL = "5min"


def convert_time_series(time_series_function):
    if time_series_function == "1":
        return "TIME_SERIES_INTRADAY"
    elif time_series_function == "2":
        return "TIME_SERIES_DAILY"
    elif time_series_function == "3":
        return "TIME_SERIES_WEEKLY"
    elif time_series_function == "4":
        return "TIME_SERIES_MONTHLY"
    else:
        return "TIME_SERIES_INTRADAY"

def construct_url(base_url, time_series, symbol, interval, api_key):
    if time_series == "TIME_SERIES_INTRADAY":
        full_url = base_url + "function=" + time_series + "&symbol=" + symbol + "&interval=" + interval + "&apikey=" + api_key
    else:
        full_url = base_url + "function=" + time_series + "&symbol=" + symbol + "&apikey=" +api_key
    
    return(full_url)
