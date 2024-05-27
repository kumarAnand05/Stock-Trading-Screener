import os
import time
import datetime
import pandas as pd
import yfinance as yf
import indicators as ind


def collect_scrip_data(stock):
    """
    Returns the time series data of NSE listed stocks.
        - Checks the local directory and updates it with the latest data
        - If local directory has no data then entire data is collected
        - If data is already up-to date then the existing data is returned without making any API call
    """

    file_path = f"stock_data/{stock}.csv"

    # Checking if file exists or not in local dir
    if os.path.exists(file_path):

        df_stored = pd.read_csv(file_path).set_index('Unnamed: 0')

        # Calculating unavailable data dates difference
        latest_available_date = df_stored.iloc[0].index[0].split(" ")[0]
        latest_available_date = datetime.datetime.strptime(latest_available_date, "%Y-%m-%d").date()

        # Finding the number of days of missing data
        current_time = datetime.datetime.now().time()
        market_opening_time = datetime.time(9, 20)
        if current_time > market_opening_time:
            latest_trading_session = datetime.date.today()
        else:
            latest_trading_session = datetime.date.today() - datetime.timedelta(days=1)

        missing_days = (latest_trading_session - latest_available_date).days        # Days of missing data
        if missing_days > 0:
            missing_data = get_latest_data(stock, str(missing_days))
            if len(missing_data.columns) == 0:
                time.sleep(5)
                missing_data = get_latest_data(stock, str(missing_days))

            # Removing existing data from collected missing data
            missed_trading_sessions = 0
            for days in range(missing_days):
                current_missing_days = (missing_data.iloc[0].index[days].date() - latest_available_date).days
                if current_missing_days > 0:
                    missed_trading_sessions += 1
                else:
                    break
            missing_data = missing_data.iloc[0:, :missed_trading_sessions]

            # Adding indicator data
            stock_data = pd.concat([missing_data, df_stored], axis=1)
            stock_data = ind.moving_averages.add_partial_ema(stock_data, missed_trading_sessions)
            stock_data = ind.rsi.add_rsi(stock_data)
            stock_data = ind.bollinger_bands.add_bollinger_bands(stock_data)

            return stock_data

        else:
            return df_stored

    # If file doesn't exist, then all data is collected
    else:
        stock_data = get_latest_data(stock, "max")
        if len(stock_data.columns) == 0:
            time.sleep(5)
            stock_data = get_latest_data(stock, "max")

        # Adding indicator data
        stock_data = ind.moving_averages.add_all_ema(stock_data)
        stock_data = ind.rsi.add_rsi(stock_data)
        stock_data = ind.bollinger_bands.add_bollinger_bands(stock_data)

        return stock_data

def get_period_value(period):
    """
    Function to set period value to overcome yFinance API issues that occur while fetching data using period args
    """
    days = int(period)
    period_map = {
        range(0, 4): '5d',
        range(4, 26): '1mo',
        range(26, 81): '3mo',
        range(81, 161): '6mo',
        range(161, 351): '1y',
        range(351, 701): '2y',
        range(701, 1751): '5y',
        range(1751, 2000): '10y',
    }

    for period_range, value in period_map.items():
        if days in period_range:
            return value
    return 'max'


def get_latest_data(stock, period):
    """ Returns the time series data of scrip for defined period of time using yfinance API """

    scrip = yf.Ticker(f"{stock}.NS")      # .NS used to specify NSE listed stocks
    # Collecting unavailable data
    if period == "max":
        latest_data = scrip.history(period='max').T.iloc[:, ::-1].round(2)
    else:
        period = get_period_value(period)
        latest_data = scrip.history(period=f'{period}').T.iloc[:, ::-1].round(2)

    # removing non-required data rows
    if "Dividends" in latest_data.index:
        latest_data = latest_data.drop('Dividends')
    if "Stock Splits" in latest_data.index:
        latest_data = latest_data.drop('Stock Splits')
    if "Volume" in latest_data.index:
        latest_data = latest_data.drop('Volume')

    return latest_data
