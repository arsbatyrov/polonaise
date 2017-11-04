import re
from poloniex import Poloniex
polo = Poloniex()

class PoloApi(object):
    polo.key = 'GHX32OJP-DGCFJKCS-LACQJUJ5-25D2KK0R'
    polo.secret = 'd51d59524afdebe60c5d19df7cbdc592446ff15fabb97c4538165b051d14654828ae670e5c6f21dd0ea1cc94a444bf2a9ac2a82138021f2f83e16abd6408c0f7'

    MIN_AMOUNT = 0.0001
    MIN_ORDER = 0.0002
    FEE = 0.25
    MIN_PROFIT = 1

    def buy(self, pair, rate, amount):
        print("I will buy the " + str(round(amount,8)) + " " + self.splitPair(pair)[1] + " for " + str(rate) + " BTC")
        # polo.buy(pair, rate, amount)

    def sell(self, pair, rate, amount):
        print("I will sell the " + str(round(amount,8)) + " " + self.splitPair(pair)[1] + " for " + str(rate) + " BTC")
        # polo.sell(pair, rate, amount)

    def values(self):
        return polo.returnTicker()

    def volume(self):
        return polo.return24hVolume()

    def lastValue(self, pair):
        allValues = self.values()
        valueForPair = allValues[pair]["last"]
        return valueForPair

    # Bid is BUY ORDER price (lower than ask)
    def getHighestBid(self, pair):
        allValues = self.values()
        bid = allValues[pair]["highestBid"]
        highestBid = round(float(bid) + 0.00000001, 8)
        return highestBid

    # Ask is SELL ORDER price (higher than bid)
    def getLowestAsk(self, pair):
        allValues = self.values()
        ask = allValues[pair]["lowestAsk"]
        lowestAsk = round(float(ask) - 0.00000001, 8)
        return lowestAsk

    def getAllBalances(self):
        allBalances = polo.returnBalances()
        return allBalances

    def getBTCBalance(self):
        allBalances = self.getAllBalances()
        btcBalance = allBalances["BTC"]
        return btcBalance

    def getAltBalance(self):
        allBalances = self.getAllBalances()
        altBalance = allBalances["BCH"]
        return altBalance

    def getChart(self, pair, period, start, end):
        data = polo.returnChartData(pair, period, start, end)
        return data

    def getOpenOrders(self, pair):
        orders = polo.returnOpenOrders(pair)
        return orders

    def splitPair(self, pair):
        splitPair = re.split(r"_", pair,)
        return splitPair


