import datetime as dt
import pandas as pd


def update_local_database(stock, data):
    """
    Download/Update collected time series data of the stock in local directory
    """

    file_path = f"stock_data/{stock}.csv"

    try:
        latest_available_date = dt.datetime.strptime(data.iloc[0].index[0].split(" ")[0], "%Y-%m-%d").date()
    except AttributeError:
        latest_available_date = data.columns[0].date()

    current_date = dt.date.today()
    current_missing_days = (current_date - latest_available_date).days      # Days of missing data

    # Excluding current day data if market is still open
    if current_missing_days == 0:
        current_time = dt.datetime.now().time()
        market_close_time = dt.time(15, 40)
        if current_time < market_close_time:
            data = data.drop(columns=data.columns[0], axis=1)

    data = data.iloc[:, :2000].round(2)     # Trimming data to last 2000 trading sessions data
    data.to_csv(file_path)

    return


def save_scanner_results(scanner_output):
    """
    Saves the collected scanner result output in csv format
    """
    
    columns = ["Stock Name",
               "Trade Signals",
               "CMP",
               "Avg Movement",
               "10D Avg Movement",
               "1W Return",
               "1M Return",
               "6M Return",
               "1Y Return",
               ]

    data = pd.DataFrame(scanner_output, columns=columns)
    data.to_csv(f'Stock Trade Signals {dt.date.today().strftime("%d")}th {dt.date.today().strftime("%b")}.csv',
                index=False)
