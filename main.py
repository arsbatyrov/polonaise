import sys
from poloApi import PoloApi
from strategy import Strategy
from ranking import Ranking
from botLog import BotLog
api = PoloApi()
strategy = Strategy()
rank = Ranking()
output = BotLog()



def main(argv):
    trade_pairs = 10
    api.closeOldOrders()
    rankedpairs = rank.getRankedPairsList()
    toppairs = rankedpairs[:trade_pairs]
    output.log("START LAUNCH")
    strategy.profitSell()
    pairs = [x for x in toppairs if x not in strategy.deletePairs]
    if not pairs:
        output.log("No new pairs found. Ending this launch.")
        return
    for i in range(0, len(pairs)):
        pair = pairs[i]
        strategy.profitBuy(pair)
    output.log("END LAUNCH")

if __name__ == "__main__":
    main(sys.argv[1:])
