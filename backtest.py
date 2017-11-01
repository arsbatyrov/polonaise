import sys, getopt

from botChart import BotChart
from botStrategy import BotStrategy
from botApi import BotApi

def main(argv):
    chart = BotChart("poloniex", "BTC_BCH", 300)

    strategy = BotStrategy()
    for candlestick in chart.getPoints():
        strategy.tick(candlestick)

if __name__ == "__main__":
    main(sys.argv[1:])