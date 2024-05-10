import numpy as np
import statistics as stats


def add_bollinger_bands(data):
    """ Adds bollinger band values to the time series data"""

    # SMA20 of the close prices
    sma20 = data.loc['Close'][::-1].rolling(window=20).mean()
    # standard deviation of closing prices for 20 periods
    sd = data.loc['Close'][::-1].rolling(window=20).apply(lambda cp: stats.stdev(cp))

    # calculating upper and lower bollinger bands
    upper_band = np.array((sma20 + (2 * sd)))[::-1]
    lower_band = np.array(sma20 - (2 * sd))[::-1]
    data.loc['Upper_bollinger'] = upper_band
    data.loc['Lower_bollinger'] = lower_band

    return data
