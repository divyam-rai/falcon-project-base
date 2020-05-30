import os
import sys

import falcon
from falcon_auth import FalconAuthMiddleware
from utils import constants as cst

os.environ['BASEPATH'] = cst.BASE_PATH
sys.path.append(cst.BASE_PATH)

from middleware.authorization import Authorization
from middleware.cors import CORSComponent
from middleware.json_translator import JSONTranslator
from middleware.require_json import RequireJSON

from endpoints.v1.test import Test

auth_middleware = FalconAuthMiddleware(Authorization(), exempt_routes=['/api/v1/test'])

api = falcon.API(middleware=[auth_middleware, CORSComponent(), JSONTranslator(), RequireJSON()])

test = Test()

ROUTES = {
    "/test" : test
}

for k,v in ROUTES.items():
    api.add_route(cst.ROUTE_PREFIX + k, v)