# app.py
from email.mime import application
from http import server
import imp
import falcon
from services.mobile_blanace_api_imp import MobileBalanceApiImp
from server_swagger import SpecServer;
router = MobileBalanceApiImp()

# operation_handlers = {
#     'getBalance': [router.getBalance]
# }

app = application = falcon.API()

# server = SpecServer(operation_handlers=operation_handlers)
# with open('conf/swagger.json') as f:
#     server.load_spec_swagger(f.read())
# app.add_sink(server , '/');
app.add_route("/phone_numbers/{phone_number}/balance", router)
# Generated by swagger???? how can i doit??