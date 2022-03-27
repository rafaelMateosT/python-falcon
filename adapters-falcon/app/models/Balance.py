from mimetypes import init
import json

from sqlalchemy import null


class Balance(object):
    amount= []
    phone_number = 0;
    currency = "EUR"
    expirationDate = null

    def __init__(self, amount,phone_number,currency,expirationDate):
        self.amount = amount
        self.phone_number = phone_number
        self.currency = currency
        self.expirationDate = expirationDate

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
        sort_keys=True, indent=4)
