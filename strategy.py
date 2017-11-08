import time
from poloApi import PoloApi
from datafiles import DataFiles
from database import Database
from botLog import BotLog
from datetime import datetime
api = PoloApi()
data = DataFiles()
db = Database()

class Strategy(object):
    def __init__(self):
        self.output = BotLog()
        self.currentPrice = 0
        self.amount = 0
        self.btcBalance = 1.00
        self.altBalance = 0.00

    def isProfit(self, pair, lastPrice):
        # get highest bid on the pair plus 1 satoshi
        hBid = float(api.getHighestBid(pair))
        # get minimum alt amount to buy for 0.0001 BTC
        amount = api.MIN_AMOUNT * hBid
        # calculate fee in ALT: amount to buy - 0.25% from it
        coinfee = amount - amount * api.FEE
        # convert fee from ALT to BTC: fee * alt price in BTC
        btcfee = round(coinfee * hBid, 8)
        # calculate profit: current price - price we bought it - fee, rounded
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # CHECK IF ASK IS THE RIGHT PRICE, NOT BID
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        profit = round(hBid - lastPrice - btcfee, 8)
        # calculate profit percent: profit / price we bought it, multiplied by 100 to get percents
        profitPercent = int(round(profit / lastPrice, 2) * 100)
        self.output.log("Highest bid is " + str(hBid) +
                        "\nLast price was " + str(lastPrice) +
                        "\nFee is " + str(btcfee) + " BTC")
        self.output.log("Total profit is " + str(profit) + ", or " + str(profitPercent) + "%.")
        if profitPercent > api.MIN_PROFIT:
            self.currentPrice = hBid
            self.amount = amount
            return True
        return False

    def tick(self, pair, wait=10):
        splitpair = api.splitPair(pair)
        # get balances on BTC and ALT
        btcBalance = round(float(api.getBTCBalance()), 8)
        altBalance = round(float(api.getAltBalance(splitpair)), 8)
        # get minimum bid for this price: 0.0001 BTC * current alt price
        minBid = api.MIN_AMOUNT * api.getHighestBid(pair)
        # get last price we bough the Alt at from database
        lastPrice = db.getLastPrice(pair)
        # if we have enough altcoins to place a minimum bid sell order
        if altBalance > minBid:
            # if we sell with profit comparing to the previous price
            if self.isProfit(pair, lastPrice):
                # sell the coin for price and amount stated in isProfit function
                self.sellAlt(pair, self.currentPrice, self.amount)
            # if this coin has been bought more than loss_time (def 2 weeks) ago
            elif self.isTooLong(pair):
                self.sellAlt(pair, self.currentPrice, self.amount)
        # we don't have enough alt, so we are going to buy it, if we have enough BTC
        elif btcBalance > api.MIN_AMOUNT:
            # get ALT amount to buy for 0.0001 BTC
            minAmount = api.MIN_AMOUNT / api.getLowestAsk(pair)
            # buy minimum amount of altcoin for lowest price
            self.buyAlt(pair, api.getLowestAsk(pair), minAmount)
        time.sleep(wait)

    def buyAlt(self, pair, price, amount):
        api.buy(pair, price, amount)

    def sellAlt(self, pair, price, amount):
        api.sell(pair, price, amount)

    def isTooLong(self, pair):
        lastTime = datetime(db.getLastTime(pair))
        timestamp = datetime.today()
        loss_time = api.LOSS_TIME * 86400.0
        if timestamp - lastTime > loss_time:
            print("loss time activated")
            return True
        return False

    # def test_profit(self, lastPrice, hBid):
    #     amount = api.MIN_AMOUNT / hBid
    #     coinfee = amount - amount * api.FEE
    #     btcfee = round(coinfee * hBid, 8)
    #     profit = round(hBid - lastPrice - btcfee, 8)
    #     profitPercent = int(round(profit / lastPrice, 2) * 100)
    #     self.output.log("Highest bid is " + str(hBid) +
    #                     "\nLast price was " + str(lastPrice) +
    #                     "\nFee is " + str(btcfee) + " BTC")
    #     self.output.log("Total profit is " + str(profit) + ", or " + str(profitPercent) + "%.")
    #     if profitPercent > api.MIN_PROFIT:
    #         self.currentPrice = hBid
    #         self.amount = amount
    #         return True
    #     return False
    #
    # def test_tick(self, pair, hBid, lAsk, wait=10):
    #     if self.altBalance > api.MIN_AMOUNT / hBid:
    #         if self.test_profit(self.lastSellPrice, hBid):
    #             self.sellAlt(pair, self.currentPrice, self.amount)
    #             self.altBalance -= self.amount
    #             self.btcBalance += self.currentPrice * self.amount
    #     elif self.btcBalance > api.MIN_AMOUNT:
    #         self.buyAlt(pair, lAsk, api.MIN_AMOUNT / lAsk)
    #         self.btcBalance -= api.MIN_AMOUNT
    #         self.altBalance += api.MIN_AMOUNT / lAsk
    #     time.sleep(wait)

