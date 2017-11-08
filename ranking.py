import json
import operator
from poloApi import PoloApi
api = PoloApi()

class Ranking(object):

    def __init__(self):
        self.ranking = {}
        pass

    def getData(self):
        # get values from api
        array = api.values()
        # technical code to convert json to dict
        dump = json.dumps(array)
        data = json.loads(dump)
        return data

    def getRankedPairsList(self):
        # get values to variable
        data = self.getData()
        # make a list of coins for further usage
        datakeys = list(data.keys())
        # select only BTC_XXX pairs. If not needed, change btckeys for datakeys variable
        btckeys = [x for x in datakeys if x.startswith('BTC')]
        # makes an unsorted pair: rank dictionary
        for i in range(1, len(btckeys)):
            pair = btckeys[i]
            # get data by pair index
            pairdata = data.get(pair)
            # get parameters to formula
            lAsk = float(pairdata.get("lowestAsk"))
            hBid = float(pairdata.get("highestBid"))
            volume = float(pairdata.get("baseVolume"))
            rank = ((lAsk - hBid) / hBid) * volume
            # remove Alt from top if cheaper than min value (100 satoshi by default)
            if hBid < api.MIN_VALUE:
                rank = 0
            # append a value to dictionary
            self.ranking[pair] = rank
        # get pair:rank list of tuples sorted by rank
        sortedRank = sorted(self.ranking.items(), key=operator.itemgetter(1), reverse=True)
        # get only sorted pairs from list
        sortedPairs = [str(i[0]) for i in sortedRank]
        return sortedPairs
