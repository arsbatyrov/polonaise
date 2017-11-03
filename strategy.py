from poloApi import PoloApi
api = PoloApi()

class Strategy(object):
    def __init__(self):
        self.prices = []
        self.trades = []
        self.currentPrice = ""
        self.numSimulTrades = 1
        self.lastBuyPrice = ""
        self.lastSellPrice = ""

    def tick(self):
        pair = "BTC_BCH"
        self.isProfit(pair)

    def isProfit(self, pair, lastPrice):
        hBid = api.getHighestBid(pair)
        amount = api.MIN_AMOUNT / hBid
        coinfee = amount / api.FEE
        btcfee = round(coinfee * hBid, 8)
        profit = round(hBid - lastPrice - btcfee, 8)
        # profitPercent = profit *
        print("Highest bid is " + str(hBid) + ", lastPrice was " + str(lastPrice) + ", and exchange comission is " + str(btcfee) + " BTC")
        print("Total profit is " + str(profit))
        if profit > 0:
            return True
        else:
            return False

    def buyAlt(self, pair, hBid):
        amount = api.MIN_AMOUNT / hBid
        api.buy(pair, hBid, amount)

    #
    # def evaluatePositions(self):
    #     pair = "BTC_BCH"
    #     volume = api.volume(api)
    #     hBid = api.getHighestBid(api, pair)
    #     lAsk = api.getLowestAsk(api, pair)
    #
    #     openTrades = []
    #     for trade in self.trades:
    #         if trade.status == "OPEN":
    #             openTrades.append(trade)

        # if(len(openTrades) < self.numSimulTrades):
                # if(self.currentPrice < )








