<h1 align="center">
   Stock Trading Screener
</h1>

This project is a python based stock screener that collects real-time data of the stocks listed on the National Stock Exchange (NSE) and does time-series analysis to generate trading signals by implementation of multiple conventional technical analysis strategies.

## Features

* **Real-time data collection** : Fetches the most recent data using yfinance API.
* **Implementation of Technical Indicators** : Calculates technical indicators data and add it to the stock data to implement different trading strategies. 
* **Downloading data** : Stores the data locally for faster processing.

#### Features under test
* **EMA crossover Strategy**
* **EMA & Price crossover strategy**
* **Support and Resistance detection**

#### Features under development
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


