import os
import sys
sys.path.append(os.getenv('BASEPATH'))

import falcon
from falcon_auth.backends import AuthBackend
from utils import constants as cst, general as hp
from utils.redis import Redis

r_redis = Redis()

logger = hp.get_logger("authorization", cst.LOGGER["authorization"])

class Authorization(AuthBackend):
    def __init__(self):
        self.user_loader = ""

    def authenticate(self, req: falcon.Request, resp: falcon.Response, resource):
        try:
            logger.info("In Authentication function")
            auth_key = req.get_header("Authorization")
            auth_session = req.get_header("sid")
            logger.info("auth_key: %s" % auth_key)
            if auth_key is None or auth_session is None:
                logger.info("No Authorization or sessionid")
                raise falcon.HTTPUnauthorized('Authorization and sessionid required', '', '', href='')
            logger.info("Checking redis for: %s" % auth_session)
            session_key = r_redis.hget(cst.REDIS_SESSION_MAP, auth_session)
            if session_key is None:
                logger.info("Session expired")
                raise falcon.HTTPUnauthorized('Session expired', '', '', href='')
            logger.info("Ready to decrypt session: %s" % session_key)
            if session_key != auth_key:
                logger.info("Invalid authorization")
                raise falcon.HTTPUnauthorized('Invalid authorization', '', '', href='')
            logger.info("Authentication successful")
            return True
        except Exception as e:
            logger.info("Error occured while authenticating: %s" % e)
            raise falcon.HTTPUnauthorized('Authorization failed', '', '', href='')


