from models.Balance import Balance

class BalanceBuilder():
    def createBalance(self , dataBalance , dataExpiration , phoneNumber):
        balanceTotal = 0;
        for data in dataBalance["balances"]:
           balanceTotal += int(data["amount"])

        return Balance(balanceTotal,phoneNumber,"EUR",dataExpiration)
