# mobile_blanace_api_imp.py
import falcon
from repositories.balance_repository import BalanceRepository
from mappers.BalanceBuilder import BalanceBuilder
from concurrent.futures import ThreadPoolExecutor

methods = BalanceRepository();
mappers = BalanceBuilder();

class MobileBalanceApiImp:
    def on_get(self, req, resp , phone_number):
        #Run in parallel
        with ThreadPoolExecutor(max_workers=2) as executor:
            futureBalance = executor.submit(methods.getBalance, phone_number)
            futureExpiration= executor.submit(methods.getExpirationBalance, phone_number)

        result = mappers.createBalance(futureBalance.result() , futureExpiration.result()['expirationDate'] , phone_number).toJSON()
        resp.body = result
        resp.status = falcon.HTTP_OK
        print(result)
