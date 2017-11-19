import configparser
config = configparser.ConfigParser()


class CommonApi(object):
    def __init__(self, exchange):
        config.read("files/config.ini")
        self.MIN_AMOUNT = float(config.get(exchange, "MIN_AMOUNT"))
        self.FEE = float(config.get(exchange, "FEE"))
        self.MIN_PROFIT = int(config.get(exchange, "MIN_PROFIT"))
        self.MIN_VALUE = float(config.get(exchange, "MIN_VALUE"))
        self.LOSS_TIME = int(config.get(exchange, "LOSS_TIME"))


