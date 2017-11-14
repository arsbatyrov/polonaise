import time
from poloApi import PoloApi
from datafiles import DataFiles
from database import Database
from botLog import BotLog
import datetime
api = PoloApi()
data = DataFiles()
db = Database()
dt = datetime

class Strategy(object):
    def __init__(self):
        self.output = BotLog()
        self.currentPrice = 0

    def isProfit(self, pair, lastPrice):
        # get highest bid on the pair minus 1 satoshi
        lAsk = float(api.getLowestAsk(pair))
        # get minimum alt amount to buy for 0.0001 BTC
        amount = api.MIN_AMOUNT / lAsk
        # calculate fee in ALT: amount to buy - 0.25% from it
        coinfee = amount * api.FEE
        # convert fee from ALT to BTC: fee * alt price in BTC
        btcfee = round(coinfee * lAsk, 8)
        # calculate profit: current price (my best price, lAsk - 1 satoshi) - price we bought it - fee, rounded
        profit = round(lAsk - lastPrice - btcfee, 8)
        # calculate profit percent: profit / price we bought it, multiplied by 100 to get percents
        profitPercent = int(round(profit / lastPrice, 2) * 100)
        self.output.log("Pair: " + pair + ". Profit is " + str(format(profit, '.8f')) + ", or " + str(profitPercent) + "%.")
        if profitPercent > api.MIN_PROFIT:
            self.currentPrice = lAsk
            self.amount = amount
            return True
        return False

    def profitSell(self):
        mycoins = api.getNotNullBalances()
        for k, v in mycoins.items():
            altName = k
            altBalance = float(v)
            pair = api.mergePair(altName)
            # get minimum bid for this price: 0.0001 BTC / current alt price
            # calculations sample: if 1 ETH = 0.25 BTC, divide 0.0001/0.25, and get 0.0004
            minBid = api.MIN_AMOUNT / api.getHighestBid(pair)
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



    def tick(self, pair, wait=0):
        splitpair = api.splitPair(pair)
        # get balances on BTC and ALT
        btcBalance = round(float(api.getBTCBalance()), 8)
        # self.output.log("BTC balance: " + str(btcBalance) + ".")
        altBalance = round(float(api.getAltBalance(splitpair)), 8)
        # self.output.log("Alt balance: " + str(altBalance) + ".")
        # get minimum bid for this price: 0.0001 BTC / current alt price
        # calculations sample: if 1 ETH = 0.25 BTC, divide 0.0001/0.25, and get 0.0004
        minBid = api.MIN_AMOUNT / api.getHighestBid(pair)
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
        else:
            # Not enough bitcoins for bot to trade
            self.output.log("\033[91m " + "NOT ENOUGH BTC" + "\033[0m")
        time.sleep(wait)

    def buyAlt(self, pair, price, amount):
        api.buy(pair, price, amount)

    def sellAlt(self, pair, price, amount):
        api.sell(pair, price, amount)

    def isTooLong(self, pair):
        lastTime = db.getLastTime(pair)
        timestamp = dt.datetime.today()
        loss_time = dt.timedelta(api.LOSS_TIME * 86400)
        if (timestamp - lastTime) > loss_time:
            self.output.log("Pair " + pair + " is sold on loss time")
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

