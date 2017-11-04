import sys
from poloApi import PoloApi
from strategy import Strategy
api = PoloApi()
strategy = Strategy()
pair = "BTC_BCH"


def main(argv):
    chart = api.getChart(pair, 300, 1509575629, 1511075629)
    strategy = Strategy
    for candlestick in chart:
        strategy.tick(pair, candlestick, 10)

if __name__ == "__main__":
    main(sys.argv[1:])