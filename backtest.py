import sys, getopt

from botChart import BotChart
from botStrategy import BotStrategy
from poloApi import poloApi

def main(argv):
    chart = BotChart("poloniex", "BTC_BCH", 300)

    strategy = BotStrategy()
    for candlestick in chart.getPoints():
        strategy.tick(candlestick)

    api = poloApi

    api.buy(poloApi, "BTC_BCH", rate, amount)

if __name__ == "__main__":
    main(sys.argv[1:])