import re
from poloApi import PoloApi
api = PoloApi

class TestInterface(object):
    def __init__(self):
        pass

    pair = "BTC_BCH"

    # get info from exchange

    volume = api.volume(api)
    values = api.values(api)

    lastValue = api.lastValue(api, pair)
    hBid = api.getHighestBid(api, pair)
    lAsk = api.getLowestAsk(api, pair)

    balances = api.getAllBalances(api)
    myBTC = api.getBTCBalance(api)
    myALT = api.getAltBalance(api)

    print("Highest bid is " + str(hBid))
    print("Lowest ask is " + str(lAsk))
    print("My BTC balance is: " + myBTC)
    print("My BCH balance is: " + myALT)

    # print(values)
    # print("Last value of " + pair + " pair is " + lastValue)
    # print("Highest bid is " + hBid + ", lowest ask is " + lAsk)

    # test buy
    # api.buy(api, "BTC_BCH", 0.07954997, 0.00001)

    # # test sell
    # api.sell(api, pair, 0.07911000, 0.00399101)
