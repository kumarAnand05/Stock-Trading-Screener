from strategies import crossover_strategies


def analyze_stock(stock_data):
    remarks = []

    # Golden crossover and death crossover strategy
    ema_crossover_signal = crossover_strategies.ema_crossover(stock_data)
    if ema_crossover_signal != 0:
        if ema_crossover_signal == 1:
            remarks.append("Golden Crossover")
        elif ema_crossover_signal == -1:
            remarks.append("Death Crossover")

    # Price and ema crossover strategy
    ema50_price_signal = crossover_strategies.price_ema50_crossover(stock_data)
    ema200_price_signal = crossover_strategies.price_ema200_crossover(stock_data)
    if ema50_price_signal != 0:
        if ema50_price_signal == -1:
            remarks.append("Price breaking EMA50 support")
        elif ema50_price_signal == 1:
            remarks.append("Price breaking EMA50 resistance")

    if ema200_price_signal != 0:
        if ema200_price_signal == -1:
            remarks.append("Price breaking EMA200 support")
        elif ema200_price_signal == 1:
            remarks.append("Price breaking EMA200 resistance")

    # Price and bollinger band crossover strategy
    bb_price_signal = crossover_strategies.bollinger_band_price_crossover(stock_data)
    if bb_price_signal == 1:
        remarks.append("Stock outside bollinger band resistance")
    elif bb_price_signal == -1:
        remarks.append("Stock outside bollinger band support")

    return remarks
