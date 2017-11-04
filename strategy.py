import time
from poloApi import PoloApi
from botLog import BotLog
api = PoloApi()


class Strategy(object):
    def __init__(self):
        self.output = BotLog()
        self.currentPrice = 0
        self.lastBuyPrice = 0.01
        self.lastSellPrice = 0.01
        self.amount = 0

    def tick(self, pair, candlestick, wait=10):
        self.currentPrice = float(candlestick["weightedAverage"])
        btcBalance = round(float(api.getBTCBalance()), 8)
        altBalance = round(float(api.getAltBalance()), 8)
        if altBalance > api.MIN_AMOUNT / api.getHighestBid(pair):
            if self.isProfit(pair, self.lastSellPrice):
                self.sellAlt(pair, self.currentPrice, self.amount)
        elif btcBalance > api.MIN_AMOUNT:
            self.buyAlt(pair, api.getLowestAsk(pair), api.MIN_AMOUNT / api.getLowestAsk(pair))
        time.sleep(wait)

    def isProfit(self, pair, lastPrice):
        hBid = api.getHighestBid(pair)
        amount = api.MIN_AMOUNT / hBid
        coinfee = amount / api.FEE
        btcfee = round(coinfee * hBid, 8)
        profit = round(hBid - lastPrice - btcfee, 8)
        profitPercent = int(round(profit / lastPrice, 2) * 100)
        print("Highest bid is " + str(hBid) + ", lastPrice was " + str(lastPrice) + ", and exchange comission is " + str(btcfee) + " BTC")
        print("Total profit is " + str(profit) + ", or " + str(profitPercent) + "%.")
        if profitPercent > api.MIN_PROFIT:
            self.currentPrice = hBid
            self.amount = amount
            return True
        return False

    def buyAlt(self, pair, price, amount):
        api.buy(pair, price, amount)
        self.lastBuyPrice = price

    def sellAlt(self, pair, price, amount):
        api.sell(pair, price, amount)
        self.lastSellPrice = price