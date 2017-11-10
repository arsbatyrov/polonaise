import logging

class BotLog(object):
    def __init__(self):
        logging.basicConfig(filename='files/bot.log', level=logging.INFO, format='%(asctime)s %(message)s')
        pass

    def log(self, message):
        print(message)
        logging.info(message)

