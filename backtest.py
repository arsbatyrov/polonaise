import sys, getopt

from botChart import BotChart
from botStrategy import BotStrategy
from poloApi import BotApi

def main(argv):
    chart = BotChart("poloniex", "BTC_BCH", 300)

    strategy = BotStrategy()
    for candlestick in chart.getPoints():
        strategy.tick(candlestick)

    api = BotApi

    api.buy(BotApi, pair, rate, amount)

if __name__ == "__main__":
    main(sys.argv[1:])