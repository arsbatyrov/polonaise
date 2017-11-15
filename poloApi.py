import re
import json
import configparser
from datetime import datetime
from poloniex import Poloniex
from datafiles import DataFiles
from database import Database
from botLog import BotLog

config = configparser.ConfigParser()
polo = Poloniex()
file = DataFiles()
db = Database()
output = BotLog()

class PoloApi(object):
    polo.key = 'GHX32OJP-DGCFJKCS-LACQJUJ5-25D2KK0R'
    polo.secret = 'd51d59524afdebe60c5d19df7cbdc592446ff15fabb97c4538165b051d14654828ae670e5c6f21dd0ea1cc94a444bf2a9ac2a82138021f2f83e16abd6408c0f7'

    def __init__(self):
        config.read("files/config.ini")
        self.MIN_AMOUNT = float(config.get("Poloniex", "MIN_AMOUNT"))
        self.FEE = float(config.get("Poloniex", "FEE"))
        self.MIN_PROFIT = int(config.get("Poloniex", "MIN_PROFIT"))
        self.MIN_VALUE = float(config.get("Poloniex", "MIN_VALUE"))
        self.LOSS_TIME = int(config.get("Poloniex", "LOSS_TIME"))

    def buy(self, pair, rate, amount):
        amount = str(format(round(amount, 8), ".8f"))
        alt = self.splitPair(pair)[1]
        rate = str(format(rate, ".8f"))
        timestamp = str(datetime.today())
        output.log("\033[91m" + "BOUGHT " + amount + " " + alt + " by the price of " + rate + " BTC for 1 " + alt +"\033[0m")
        db.writePrice(pair, timestamp, rate)
        polo.buy(pair, rate, amount)

    def sell(self, pair, rate, amount):
        amount = str(format(round(amount, 8), ".8f"))
        alt = self.splitPair(pair)[1]
        rate = str(format(rate, ".8f"))
        output.log("\033[92m" + "SOLD " + amount + " " + alt + " by the price of " + rate + " BTC for 1 " + alt + "\033[0m")
        polo.sell(pair, rate, amount)

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

    def getNotNullBalances(self):
        allbalances = self.getAllBalances()
        balances = dict((k, v) for k, v in allbalances.items() if v != '0.00000000')
        balances.pop('BTC')
        return balances

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

    def mergePair(self, alt):
        mergePair = "BTC_" + alt
        return mergePair

    def getOrders(self):
        array = polo.returnOpenOrders('all')
        dump = json.dumps(array)
        data = json.loads(dump)
        return data

    def closeOldOrders(self):
        data = self.getOrders()
        # test data
        # data = dict({'BTC_BTM': [{'orderNumber':'120466','type':'sell','rate':'0.025','amount':'100','total':'2.5'}], 'BTC_SYS': [{'orderNumber':'120466','type':'sell','rate':'0.025','amount':'100','total':'2.5'},{'orderNumber':'120467','type':'sell','rate':'0.04','amount':'100','total':'4'}], 'USDT_XMR': []})
        for key, value in data.items():
            if not value == []:
                for value in data[key]:
                    orderNum = (value['orderNumber'])
                    price = self.getHighestBid(key)
                    try:
                        polo.moveOrder(orderNum, price)
                        output.log("Old order " + orderNum + " was moved to price " + str(
                            format(price, '.8f')) + " for one " + key + ".")
                        break
                    except:
                        polo.cancelOrder(orderNum)
                        output.log("Old order " + orderNum + " was cancelled as all " + key + "s cost less than min bid.")
        output.log("All old orders were closed.")
