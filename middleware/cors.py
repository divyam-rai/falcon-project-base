import os
import sys
sys.path.append(os.getenv('BASEPATH'))
import falcon
import json


class CORSComponent(object):

    def process_request(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Methods', 'DELETE, PUT, POST, GET')
        resp.set_header('Access-Control-Allow-Headers', 'content-type, sid, Authorization')
        resp.set_header('Access-Control-Expose-Headers', '*')
        resp.set_header('Access-Control-Max-Age', 1728000)  # 20 days
        if req.method == 'OPTIONS':
            raise falcon.HTTPStatus(falcon.HTTP_200, body='\n')

    def process_response(self, req, resp, resource, req_succeeded):
        if 'result' not in resp.context:
            return
        resp.body = json.dumps(resp.context['result'])
