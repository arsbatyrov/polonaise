from poloniex import Poloniex

class BotChart(object):
    def __init__(self, exchange, pair, period):
        self.conn = Poloniex('GHX32OJP-DGCFJKCS-LACQJUJ5-25D2KK0R', 'd51d59524afdebe60c5d19df7cbdc592446ff15fabb97c4538165b051d14654828ae670e5c6f21dd0ea1cc94a444bf2a9ac2a82138021f2f83e16abd6408c0f7')

        self.pair = pair
        self.period = period

        self.startTime = 1491048000
        self.endTime = 1491591200

        self.data = self.conn.returnChartData(self.pair, self.period, self.startTime, self.endTime)

    def getPoints(self):
        return self.data