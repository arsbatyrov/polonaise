import csv
csv.register_dialect('myDialect', delimiter=';', quoting=csv.QUOTE_NONE)

class DataFiles(object):
    def __init__(self):
        pass

    def readFromFile(self, pair):
        file = open(pair + '.csv', 'r+')
        data = file.read()
        print(data)
        file.close()
        return data

    def writeToFile(self, pair, rate, time):
        data = [pair, time, format(rate, '.8f')]
        with open(pair + '.csv', 'w+') as csvfile:
            writer = csv.writer(csvfile, dialect='myDialect')
            writer.writerow(data)

    def getLastPrice(self, pair):
        data = self.readFromFile(pair)
        print(data)
        for row in data:
            lastPrice = round(float(row[1]), 8)
            return lastPrice

    def isPairPresent(self, pair):
        regex = pair
        print(regex)
        with open("exchangedata.csv") as f:
            if pair in f:
                return True
            return False

