import pandas as pd
import pandas_ta as pta


def add_rsi(data):
    """ Adds calculated rsi14 data for latest 14 trading session of time series data """

    if "RSI" not in data.index:
        # Adding empty rows in dataframe for RSI
        rsi = pd.Series(dtype='float64', name='RSI', index=data.columns)
        data = pd.concat([data, rsi.to_frame().T])

    # Calculating RSI values of last 14 trading session
    rsi14 = pta.rsi(data.loc['Close'][::-1], length=14)[::-1]

    # Adding rsi data in dataframe
    for r in range(len(rsi14)):
        data.iloc[6, r] = rsi14.iloc[r]

    return data
