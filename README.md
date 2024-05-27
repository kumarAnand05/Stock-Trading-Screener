<h1 align="center">
   Stock Trading Screener
</h1>

A python based stock screener that collects real-time data of stocks listed on the [National Stock Exchange (NSE)](https://www.nseindia.com/) and performs time-series analysis to generate actionable trading signals by implementation of multiple conventional technical analysis strategies using indicators, candlestick chart and chart patterns.

## Features

* **Real-time data collection** : Fetches the most recent data using [yfinance API](https://github.com/ranaroussi/yfinance).
* **Implementation of Technical Indicators** : Calculates technical indicators data and add it to the stock data to implement different trading strategies. 
* **Downloading data** : Stores the data locally for faster processing.

#### Features under test
* **EMA crossover Strategy**
* **EMA & Price crossover strategy**
* **Support and Resistance detection**

#### Features under development
* **Candlestick Pattern Detection**
* **Chart Pattern detection**

## Installation

Download the project files or clone the project using git on your local machine
```bash
  git clone https://github.com/kumarAnand05/Stock-Trading-Screener.git
```
Make sure you have [Python](https://www.python.org) and an IDE like [VSCode](https://code.visualstudio.com), [PyCharm](https://www.jetbrains.com/pycharm) etc. installed on your machine.

Now open the project in any IDE of your choice.

> Download required libraries

The project uses different libraries that needs to be installed on your machine in order to use the project.

Use the ```requirements.txt``` file to install the dependencies.

First connect to internet and open the terminal in the project directory. Now make sure you are in your project directory and use the following code to download the dependencies using ```requirement.txt```
```bash
  pip install -r .\requirements.txt
```

###### Your machine is ready now!!! Keep machine connected to internet and run the main.py file


## Available Indicators and Strategies

### Available Indicators
* [Bollinger Bands](https://www.investopedia.com/terms/b/bollingerbands.asp)
* [50 Day EMA](https://www.investopedia.com/articles/active-trading/011415/strategies-applications-behind-50day-ema.asp)
* [EMA200](https://www.investopedia.com/terms/e/ema.asp)
* [RSI14](https://www.investopedia.com/terms/r/rsi.asp)

### Available Strategies
* [Golden Crossover](https://www.investopedia.com/terms/g/goldencross.asp)
* [Death Crossover](https://www.investopedia.com/terms/d/deathcross.asp)
* [Price-EMA Crossover](https://www.investopedia.com/articles/active-trading/052014/how-use-moving-average-buy-stocks.asp)
* [Bollinger-Band Strategy](https://hmarkets.com/learn-to-trade/learning-hub/bollinger-bands)