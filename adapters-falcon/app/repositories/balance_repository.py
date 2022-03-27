from decouple import config
import requests
import logging

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s',)

class BalanceRepository():

    def getBalance(self , phoneNumber):
        baseURL = config('baseURL')
        balancePath = config('balancePath')
        URL = baseURL + balancePath + "/" + phoneNumber + "/" + "balance"
        r = requests.get(URL)
        data = r.json()
        return data;


    def getExpirationBalance(self , phoneNumber):
        baseURL = config('baseURL2')
        balancePath = config('balancePath')
        URL = baseURL + balancePath + "/" + phoneNumber + "/" + "expirationBalance"
        r = requests.get(URL)
        data = r.json()
        return data;
