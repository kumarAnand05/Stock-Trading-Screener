from ticker_info import stock_list
from ticker_info import download_data
from ticker_info import ticker_data as td

scanned_stocks = 0
total_stocks = len(stock_list.nse_stocks)

for stock in stock_list.nse_stocks:
    scanned_stocks += 1

    try:
        stock_data = td.collect_scrip_data(stock)
        download_data.update_local_database(stock, stock_data)
    except IndexError:
        print(f"Unable to collect data for {stock}")
        continue
    except TypeError:
        print(f"Some unexpected error occurred while fetching data for {stock}")

    print(f"Data collected for {stock}, {total_stocks-scanned_stocks} remaining")
