from ..common.config import ALPHAVANATGE_API_KEY


def base_query():
    return "https://www.alphavantage.co/query?"


def check_existing_symbol(symbol):
    """Check if symbol exist in alphavantage database
    Args:
        symbol (String): Equity name

    Returns:
        Boolean: time_series_intraday request
    """


def quote_endpoint(symbol):
    """Time Series Intraday
    Args:
        symbol (String): Equity name

    Returns:
        String: time_series_intraday request
    """
    return f"{base_query}function=GLOBAL_QUOTE&symbol={symbol}&apikey={ALPHAVANATGE_API_KEY}"
