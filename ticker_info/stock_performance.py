import numpy as np


def get_stock_performance(stock_data):
    """
    Returns the calculated stock performance of the stock data
    """
    cmp = stock_data.loc['Close'].iloc[0]

    avg_movement = round((np.sum(stock_data.loc['High']) - np.sum(stock_data.loc['Low'])) / len(stock_data.columns), 2)
    avg_10day_movement = round((np.sum(stock_data.loc['High'][:10]) - np.sum(stock_data.loc['Low'][:10])) / 10, 2)

    try:
        weekly_return = f"{round(((cmp * 100) / stock_data.loc['Close'].iloc[6]) - 100, 2)}%"
    except IndexError:
        weekly_return = 'NA'

    try:
        monthly_return = f"{round(((cmp * 100) / stock_data.loc['Close'].iloc[31]) - 100, 2)}%"
    except IndexError:
        monthly_return = 'NA'

    try:
        half_yearly_return = f"{round(((cmp * 100) / stock_data.loc['Close'].iloc[181]) - 100, 2)}%"
    except IndexError:
        half_yearly_return = 'NA'

    try:
        yearly_return = f"{round(((cmp * 100) / stock_data.loc['Close'].iloc[365]) - 100, 2)}%"
    except IndexError:
        yearly_return = 'NA'

    return [cmp, avg_movement, avg_10day_movement, weekly_return, monthly_return, half_yearly_return, yearly_return]
