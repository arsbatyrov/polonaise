from poloApi import PoloApi
api = PoloApi

class Strategy(object):
    def __init__(self):
        self.prices = []
        self.trades = []
        self.currentPrice = ""
        self.numSimulTrades = 1
        self.lastBuyPrice = ""
        self.lastSellPrice = ""



    def evaluatePositions(self):
        pair = "BTC_BCH"
        volume = api.volume(api)
        hBid = api.getHighestBid(api, pair)
        lAsk = api.getLowestAsk(api, pair)

        openTrades = []
        for trade in self.trades:
            if trade.status == "OPEN":
                openTrades.append(trade)

        # if(len(openTrades) < self.numSimulTrades):
                # if(self.currentPrice < )

    def isProfit(self):
        pair = "BTC_BCH"
        volume = api.volume(api)
        hBid = api.getHighestBid(api, pair)
        lAsk = api.getLowestAsk(api, pair)
        comission = 0.0025
        minProfit = 0.02

        profit = (lAsk - hBid)/hBid * (volume[pair]["BCH"])







