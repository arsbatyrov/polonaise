from poloniex import Poloniex
polo = Poloniex()

class BotApi(object):
    polo.key = 'GHX32OJP-DGCFJKCS-LACQJUJ5-25D2KK0R'
    polo.secret = 'd51d59524afdebe60c5d19df7cbdc592446ff15fabb97c4538165b051d14654828ae670e5c6f21dd0ea1cc94a444bf2a9ac2a82138021f2f83e16abd6408c0f7'

    def buy (self, pair, rate, amount):
        if amount > 0.0001:
            amount = 0.0001
        polo.buy(pair, rate, amount)

    polo.buy("BTC_BCH", 0.07662897, 0.002)
