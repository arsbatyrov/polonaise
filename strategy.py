from poloApi import PoloApi
api = PoloApi()

class Strategy(object):
    def __init__(self):
        self.prices = []
        self.trades = []
        self.currentPrice = ""
        self.lastBuyPrice = 0.08000000
        self.lastSellPrice = ""
        self.amount = ""
        self.numSimulTrades = 1


    def tick(self, pair):
        if self.isProfit(pair, self.lastBuyPrice):
            self.buyAlt(pair, self.currentPrice, self.amount)


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
        else:
            return False

    def buyAlt(self, pair, price, amount):
        api.buy(pair, price, amount)

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








