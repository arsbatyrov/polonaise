import sys
from poloApi import PoloApi
from strategy import Strategy
from botStrategy import BotStrategy
api = PoloApi
strategy = Strategy()
pair = "BTC_BCH"


def main(argv):
    chart = api.getChart(api,"poloniex", pair, 300)
    strategy = BotStrategy()
    for candlestick in chart.getPoints():
        strategy.tick(candlestick)

if __name__ == "__main__":
    main(sys.argv[1:])