from tempfile import NamedTemporaryFile
import csv
import shutil
filename = 'exchangedata.csv'
tempfile = NamedTemporaryFile(mode='w', delete=False)
fields = ['pair', 'datetime', 'price']
csv.register_dialect('myDialect', delimiter=';', quoting=csv.QUOTE_NONE)

class DataFiles(object):
    def __init__(self):
        pass


    # def readFile(self):
        # with open('exchangedata.csv', 'r+') as exchangefile:
        #     filereader = csv.reader(exchangefile, delimiter=';', quotechar='"')
        #     for row in filereader:

    def readFromFile(self, pair):
        file = open('prices/' + pair + '.csv', 'r+')
        data = file.read()
        file.close()
        return data

    def writeToFile(self, pair, rate, time):
        data = [pair, time, format(rate, '.8f')]
        with open('prices/' + pair + '.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, dialect='myDialect')
            writer.writerow(data)


    # def writeToFile(self, pair, rate, time):
    #     with open(filename, 'w+') as csvfile, tempfile:
    #         reader = csv.DictReader(csvfile, fieldnames=fields)
    #         writer = csv.DictWriter(tempfile, fieldnames=fields)
    #         for row in reader:
    #             if row['pair'] == str(pair):
    #                 print('updating row ', row['pair'])
    #                 row['price'], row['datetime'] = rate, time
    #             row = {'pair': row['pair'], 'price': row['price'], 'datetime': row['datetime']}
    #             writer.writerow(row)
    #     shutil.move(tempfile.name, filename)
    #


        # with open('exchangedata.csv', 'w+') as exchangefile:
        #     reader = csv.reader(exchangefile)
        #     for row in reader:
        #         if row[0] = pair:




        # file = open('exchangedata.csv', 'a+')
        # if self.isPairPresent(pair):
        #     print("pair found")
        # else:
        #     message = str(pair) + ";" + str(format(rate, ".8f")) + ";" + time + ";\n"
        #     file.write(message)

    def isPairPresent(self, pair):
        regex = pair
        print(regex)
        with open("exchangedata.csv") as f:
            if pair in f:
                return True
            return False

