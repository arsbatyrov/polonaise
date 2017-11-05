from collections import defaultdict
from poloApi import PoloApi
api = PoloApi()

class Ranking(object):

    def __init__(self):
        pass

    def getData(self):
        values = ["a", "b", "c", "d"]
        pairs = {}
        print(values)
        for i in range(0, len(values)):
            pairs.update(values)
            i += 1
        print(pairs)