import os
import sys
sys.path.append(os.getenv('BASEPATH'))

import json
import falcon


class JSONTranslator(object):

    def process_request(self, req, resp):
        if req.content_length in (None, 0):
            return
        body = req.stream.read()
        if not body:
            raise falcon.HTTPBadRequest('Empty request body', 'A valid JSON document is required')
        try:
            req.context['doc'] = json.loads(body.decode('utf-8'))
        except (ValueError, UnicodeDecodeError):
            raise falcon.HTTPError(falcon.HTTP_753,'Malformed JSON', 'Could not decode the request body.The JSON was incorrect or not encoded as UTF-8.')
