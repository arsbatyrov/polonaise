import sys
from poloApi import PoloApi
from strategy import Strategy
from ranking import Ranking
api = PoloApi()
strategy = Strategy()
rank = Ranking()


def main(argv):
    trade_pairs = 10
    api.closeOldOrders()
    pairs = rank.getRankedPairsList()
    for i in range(0, trade_pairs):
        pair = pairs[i]
        strategy.tick(pair, 0)

if __name__ == "__main__":
    main(sys.argv[1:])
