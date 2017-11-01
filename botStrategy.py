from botLog import BotLog
from botIndicators import BotIndicators
from botTrade import BotTrade

class BotStrategy(object):
    def __init__(self):
        self.output = BotLog()
        self.prices = []
        self.trades = []
        self.currentPrice = ""
        self.numSimulTrades = 1

        self.indicators = BotIndicators()

    def tick(self,candlestick):
        self.currentPrice = float(candlestick["weightedAverage"])
        self.prices.append(self.currentPrice)

        self.output.log("Price: "+str(candlestick["weightedAverage"]))

        self.evaluatePositions()

        self.showPositions()

    def evaluatePositions(self):
        openTrades = []
        for trade in self.trades:
            if (trade.status == "OPEN"):
                openTrades.append(trade)

        if len(openTrades) < self.numSimulTrades:
            if self.currentPrice < self.indicators.movingAverage(self.prices,15):
                self.trades.append(BotTrade(self.currentPrice))

        for trade in openTrades:
            if self.currentPrice > self.indicators.movingAverage(self.prices,15):
                trade.close(self.currentPrice)

    def showPositions(self):
        for trade in self.trades:
            trade.showTrade()