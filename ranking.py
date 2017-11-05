import json
from poloApi import PoloApi
api = PoloApi()

class Ranking(object):

    def __init__(self):
        self.rank = []
        pass

    def getData(self):
        array = api.values()
        dump = json.dumps(array)
        data = json.loads(dump)
        return data

    def getRankList(self):
        data = self.getData()
        datakeys = list(data.keys())
        for i in range(1, len(datakeys)):
            pair = datakeys[i]
            pairdata = data.get(pair)
            lAsk = float(pairdata.get("lowestAsk"))
            hBid = float(pairdata.get("highestBid"))
            volume = float(pairdata.get("baseVolume"))
            rank = ((lAsk - hBid) / hBid) * volume
            self.rank.append(rank)

    def sortRank(self):
        self.rank.sort()



