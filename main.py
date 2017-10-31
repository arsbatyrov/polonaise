import time
import sys, getopt
import datetime
from poloniex import Poloniex
polo = Poloniex()

polo.key = 'GHX32OJP-DGCFJKCS-LACQJUJ5-25D2KK0R'
polo.secret = 'd51d59524afdebe60c5d19df7cbdc592446ff15fabb97c4538165b051d14654828ae670e5c6f21dd0ea1cc94a444bf2a9ac2a82138021f2f83e16abd6408c0f7'

balance = polo.returnBalances()
print("I have %s BTC!" % balance['BTC'])
volume = polo.return24hVolume();
print (volume)
