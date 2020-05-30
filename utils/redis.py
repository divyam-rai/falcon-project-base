import os
import sys
sys.path.append(os.getenv('BASEPATH'))

import redis
from utils import constants as cst

r_pool = redis.ConnectionPool(host=cst.REDIS_HOST, port=cst.REDIS_PORT, db=5)

class Redis:
    def __init__(self):
        self.r_redis = redis.Redis(connection_pool=r_pool)

    def get(self, key = None):
        return self.r_redis.get(key)
    
    def hget(self, hmap, key):
        return self.r_redis.hget(hmap, key)
    
    def exists(self, key):
        return self.r_redis.exists(key)
    
    def hexists(self, hmap, key):
        return self.r_redis.hexists(hmap, key)
    
    def set(self, key, value):
        self.r_redis.set(hmap, key, value)
        return True
    
    def hset(self, hmap, key, value):
        self.r_redis.hset(hmap, key, value)
        return True
    
