from ticker_info import stock_list
from ticker_info import download_data
from ticker_info import ticker_data as td
from ticker_info import stock_performance
from strategies import technical_analysis

scanned_stocks = 0
total_stocks = len(stock_list.nse_stocks)
scanner_output = []

for stock in stock_list.nse_stocks:
    scanned_stocks += 1
    stock_analysis = []

    try:
        stock_data = td.collect_scrip_data(stock)
        download_data.update_local_database(stock, stock_data)
        remarks = technical_analysis.analyze_stock(stock_data)
        
        if len(remarks) != 0:
            stock_analysis.append(stock)
            stock_analysis.append(" | ".join(remarks))
            stock_analysis.extend(stock_performance.get_stock_performance(stock_data))
            scanner_output.append(stock_analysis)

    except IndexError:
        print(f"Unable to collect data for {stock}")
        continue
    except TypeError:
        print(f"Some unexpected error occurred while fetching data for {stock}")

    print(f"Scanned {stock}, {total_stocks-scanned_stocks} remaining")

if len(scanner_output) != 0:
    download_data.save_scanner_results(scanner_output)
    print("\nAll possible trade signals scanned!")
else:
    print("\nNo possible trade signals found for selected stocks!")
