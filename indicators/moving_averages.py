import pandas as pd


# Multipliers for EMA calculation
alpha = 2 / (50 + 1)  # EMA50 Multiplier
beta = 2 / (200 + 1)  # EMA200 Multiplier


def add_all_ema(data):
    """ Adds calculated EMA50 and EMA200 values for the entire time series data """

    # Closing prices of last 200 trading sessions for SMA calculation
    close_prices = data.iloc[3, -201:]

    # SMA50 and SMA200 calculation
    sma50 = round(sum(close_prices[-50:]) / 50, 2)
    sma200 = round(sum(close_prices[-200:]) / 200, 2)

    # Adding empty rows in dataframe for EMA50 and EMA200
    ema50 = pd.Series(dtype='float64', name='EMA50', index=data.columns)
    ema200 = pd.Series(dtype='float64', name='EMA200', index=data.columns)
    data = pd.concat([data, ema50.to_frame().T, ema200.to_frame().T])

    # Setting last 50SMA as last 50EMA and 200SMA as last 200EMA
    data.iloc[4, -1] = sma50
    data.iloc[5, -1] = sma200

    # EMA Calculation and addition to dataframe
    for i in range(len(data.loc['EMA200']) - 2, -1, -1):
        """ -2 because looping starts from second last value
        as first is already set to SMA. """

        prev_50ema = data.iloc[4, i + 1]
        prev_200ema = data.iloc[5, i + 1]
        close = data.iloc[3, i]

        data.iloc[4, i] = round((close * alpha) + (prev_50ema * (1 - alpha)), 2)
        data.iloc[5, i] = round((close * beta) + (prev_200ema * (1 - beta)), 2)

    return data


def add_partial_ema(data, missed_trading_sessions):
    """ Adds calculated EMA50 and EMA200 values for unavailable trading session time series data """

    for i in range(missed_trading_sessions - 1, -1, -1):
        prev_50ema = data.iloc[4, i + 1]
        prev_200ema = data.iloc[5, i + 1]

        close = data.iloc[3, i]
        data.iloc[4, i] = round((close * alpha) + (prev_50ema * (1 - alpha)), 2)
        data.iloc[5, i] = round((close * beta) + (prev_200ema * (1 - beta)), 2)

    return data
