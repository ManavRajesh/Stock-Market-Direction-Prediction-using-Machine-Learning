def trading_simulation(prices, predictions, cost=0.001):
    capital = 1.0

    for i in range(len(predictions)-1):
        if predictions[i] == 1:
            ret = (prices[i+1] - prices[i]) / prices[i]
            capital *= (1 + ret - cost)

    return capital
