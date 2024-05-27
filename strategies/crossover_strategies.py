from chart_utilities import intersection

trading_sessions = 7


def ema_crossover(stock_data):
    """
    Checks for a golden/death crossover on the chart within the defined trading period
    return :
                -1 if death crossover (downtrend)
                0 if no crossover
                1 if golden crossover (uptrend)
    """

    return intersection.check_crossover(stock_data.loc['EMA50'], stock_data.loc['EMA200'], trading_sessions)


def price_ema50_crossover(stock_data):
    """
    Checks whether there is a crossover of price and ema50.
    returns :
                -1 if price crosses ema50 from upside (downtrend)
                0 if price and ema50 crossover not happening
                1 if price crosses ema50 from downside (uptrend)
    """

    return intersection.check_crossover(stock_data.loc['Close'], stock_data.loc['EMA50'], trading_sessions)


def price_ema200_crossover(stock_data):
    """
    Checks whether there is a crossover of price and ema200.
    returns :
                -1 if price crosses ema200 from upside (downtrend)
                0 if price and ema200 crossover not happening
                1 if price crosses ema200 from downside (uptrend)
    """

    return intersection.check_crossover(stock_data.loc['Close'], stock_data.loc['EMA200'], trading_sessions)


def bollinger_band_price_crossover(stock_data):
    """
    Checks whether there is a crossover of price and bollinger bands.
    returns :
                -1 if price crosses lower bollinger band (downtrend)
                0 if price and bollinger band crossover not happening
                1 if price crosses upper bollinger band (uptrend)
    """

    if intersection.check_crossover(stock_data.loc['Close'], stock_data.loc['Upper_bollinger'], trading_sessions) == 1:
        return 1

    if intersection.check_crossover(stock_data.loc['Close'], stock_data.loc['Lower_bollinger'], trading_sessions) == -1:
        return -1

    return 0
