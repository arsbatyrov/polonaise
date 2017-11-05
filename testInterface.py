import json
from poloApi import PoloApi
from strategy import Strategy
from botChart import BotChart
api = PoloApi()
strategy = Strategy()
chart = BotChart("poloniex", "BTC_BCH", 300)

class TestInterface(object):
    def __init__(self):
        self.rank = []


    array = api.values()
    dump = json.dumps(array)
    data = json.loads(dump)
    datakeys = list(data.keys())
    for i in range(1, len(datakeys)):
        pair = datakeys[i]
        pairdata = data.get(pair)
        lAsk = float(pairdata.get("lowestAsk"))
        hBid = float(pairdata.get("highestBid"))
        volume = float(pairdata.get("baseVolume"))
        rank = ((lAsk - hBid)/hBid)*volume
        self.rank = rank

        print(pair + " " + str(rank))


    # points = chart.getPoints()
    # print(len(points))
    # for i in range(0, len(points)):
    #     hBid = float(points[i]["high"])
    #     lAsk = float(points[i]["low"])
    #     strategy.test_tick(pair, hBid, lAsk, 0)
    #     i += 1
    # print(str(strategy.altBalance) + " BCH")
    # print(str(strategy.btcBalance) + " BTC")


    # while True:
    #     strategy.tick(pair)

    # get info from exchange

    # api.splitPair(pair)
    # profit = strategy.isProfit(pair, lastBuyPrice)
    # print(profit)

    # strategy.tick(pair)

    # volume = float(api.volume(api))
    # values = float(api.values(api))

    # lastValue = api.lastValue(api, pair)
    # hBid = float(api.getHighestBid(api, pair))
    # lAsk = float(api.getLowestAsk(api, pair))

    # balances = api.getAllBalances()
    # myBTC = api.getBTCBalance()
    # myALT = api.getAltBalance()
    #
    # print("Highest bid is " + str(hBid))
    # print("Lowest ask is " + str(lAsk))
    # print("My BTC balance is: " + myBTC)
    # print("My BCH balance is: " + myALT)
    #
    # print(volume[pair]["BCH"])

    # print(values)
    # print("Last value of " + pair + " pair is " + lastValue)
    # print("Highest bid is " + hBid + ", lowest ask is " + lAsk)

    # test buy
    # api.buy(api, "BTC_BCH", 0.07954997, 0.00001)

    # # test sell
    # api.sell(api, pair, 0.07911000, 0.00399101)
    #
    # range = (lAsk - hBid) / hBid * volume[pair]["BCH"]
    # delta = lAsk - lastBuyPrice
    # profit = delta - (lAsk * api.FEE)
    # print(profit)