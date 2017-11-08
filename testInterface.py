from poloApi import PoloApi
from strategy import Strategy
from ranking import Ranking
from datafiles import DataFiles
from database import Database
api = PoloApi()
strategy = Strategy()
rank = Ranking()
file = DataFiles()
db = Database()


class TestInterface(object):
    def __init__(self):
        pass