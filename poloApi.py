import re
import json
from datetime import datetime
from poloniex import Poloniex
from datafiles import DataFiles
from database import Database
polo = Poloniex()
file = DataFiles()
db = Database()

class PoloApi(object):
    polo.key = 'GHX32OJP-DGCFJKCS-LACQJUJ5-25D2KK0R'
    polo.secret = 'd51d59524afdebe60c5d19df7cbdc592446ff15fabb97c4538165b051d14654828ae670e5c6f21dd0ea1cc94a444bf2a9ac2a82138021f2f83e16abd6408c0f7'

    MIN_AMOUNT = 0.0001
    MIN_ORDER = 0.0002
    FEE = 0.0025
    MIN_PROFIT = 1
    MIN_VALUE = 0.000001
    LOSS_TIME = 14

    def buy(self, pair, rate, amount):
        alt = self.splitPair(pair)[1]
        timestamp = str(datetime.today())
        print("I will buy the " + str(format(round(amount, 8), ".8f")) + " " + alt + " by the price of " + str(format(rate, ".8f")) + " BTC for 1 " + alt)
        db.writePrice(pair, timestamp, rate)
        # polo.buy(pair, rate, amount)

    def sell(self, pair, rate, amount):
        alt = self.splitPair(pair)[1]
        print("I will sell the " + str(format(round(amount, 8), ".8f")) + " " + alt + " by the price of " + str(format(rate, ".8f")) + " BTC for 1 " + alt)
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

    def getAltBalance(self, splitPair):
        allBalances = self.getAllBalances()
        altBalance = allBalances[splitPair[1]]
        return altBalance

    def getChart(self, pair, period, start, end):
        data = polo.returnChartData(pair, period, start, end)
        return data

    def getOpenOrders(self, pair):
        orders = polo.returnOpenOrders(pair)
        return orders

    # Splits coin pair "BTC_ETH" to "BTC, ETC"
    def splitPair(self, pair):
        splitPair = re.split(r"_", pair,)
        return splitPair

    def getOrders(self):
        array = polo.returnOpenOrders('all')
        dump = json.dumps(array)
        data = json.loads(dump)
        return data

    def closeOldOrders(self):
        data = self.getOrders()
        price = 0
        # test data
        data = "{'BTC_BTM': [], 'BTC_SYS': [{'orderNumber':'120466','type':'sell','rate':'0.025','amount':'100','total':'2.5'},{'orderNumber':'120467','type':'sell','rate':'0.04','amount':'100','total':'4'}], 'USDT_XMR': []}"
        print(data)
        ordernumber=0
        polo.moveOrder(ordernumber,price)



