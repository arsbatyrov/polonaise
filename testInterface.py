from poloApi import PoloApi
api = PoloApi

class TestInterface(object):
    def __init__(self):
        pass

    pair = "BTC_BCH"

    # get info from exchange

    lastBuyPrice = 0.09000000

    volume = float(api.volume(api))
    values = float(api.values(api))

    # lastValue = api.lastValue(api, pair)
    hBid = float(api.getHighestBid(api, pair))
    lAsk = float(api.getLowestAsk(api, pair))

    # balances = api.getAllBalances(api)
    # myBTC = api.getBTCBalance(api)
    # myALT = api.getAltBalance(api)
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

    range = (lAsk - hBid) / hBid * volume[pair]["BCH"]
    profit = lAsk - lastBuyPrice
    print(profit)