from botLog import BotLog

class BotTrade(object):
    def __init__(self, currentPrice):
        self.output = BotLog()
        self.status = "OPEN"
        self.entryPrice = currentPrice
        self.exitPrice = ""
        self.output.log("Trade opened")

    def close(self, currentPrice):
        self.status = "CLOSED"
        self.exitPrice = currentPrice
        self.output.log("Trade closed")

    def showTrade(self):
        tradeStatus = "Entry price: "+str(self.entryPrice)+" Status: "+str(self.status)+" Exit price: "+str(self.exitPrice)

        if (self.status == "CLOSED"):
            tradeStatus = tradeStatus + " Profit: "
            if (self.exitPrice > self.entryPrice):
                tradeStatus = tradeStatus + "\033[92m"
            else:
                tradeStatus = tradeStatus + "\033[91m"

            # tradeStatus = tradeStatus+str(self.exitPrice - self.entryPrice+"\033[0m")

        self.output.log(tradeStatus)