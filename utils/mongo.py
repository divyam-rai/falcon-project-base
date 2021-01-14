import os
import sys
sys.path.append(os.getenv('BASEPATH'))
from utils import constants as cst, helpers as hp
import pymongo
from pymongo.errors import BulkWriteError
from pymongo.errors import ConnectionFailure, OperationFailure

client = pymongo.MongoClient(host=cst.MONGO_CLIENT, replicaSet=cst.MONGO_REPLICA_SET)

def get_one(username, pwd, database, collection, condition, logger):
    try:
        db = getattr(client, database)
        db.authenticate(username, pwd)
        res = db[collection].find_one(condition, {'_id': False})
        db.logout()
        return res
    except Exception as e:
        logger.info(str(e))
        return False

def get_all(username, pwd, database, collection, condition, logger):
    try:
        db = getattr(client, database)
        db.authenticate(username, pwd)
        res = list(db[collection].find(condition, {'_id': False}))
        db.logout()
        return res
    except Exception as e:
        logger.info(str(e))
        return False

def remove(username, pwd, database, collection, condition, logger):
    try:
        db = getattr(client, database)
        db.authenticate(username, pwd)
        res = db[collection].remove(condition)
        db.logout()
        return True
    except Exception as e:
        logger.info(str(e))
        return False

def count(username, pwd, database, collection, condition, logger):
    try:
        db = getattr(client, database)
        db.authenticate(username, pwd)
        res = db[collection].count_documents(condition)
        db.logout()
        return res
    except Exception as e:
        logger.info(str(e))
        return False

def aggregate(username, pwd, database, collection, logger, match=None, lookup=None, unset=None, limit=None, skip=None, group=None, sort=None, project=None):
    try:
        db = getattr(client, database)
        db.authenticate(username, pwd)
        aggregation = []
        if match is not None:
            aggregation.append({'$match' : match})
        if lookup is not None:
            for single in lookup:
                aggregation.append({'$lookup' : single})
        if group is not None:
            aggregation.append({'$group' : group})
        if skip is not None:
            aggregation.append({'$skip' : skip})
        if limit is not None:
            aggregation.append({'$limit' : limit})
        if unset is not None:
            aggregation.append({'$unset' : unset})
        if sort is not None:
            aggregation.append({'$sort' : sort})
        if project is not None:
            aggregation.append({'$project' : project})
        aggregation.append({'$project' : {"_id" : 0}})
        res = list(db[collection].aggregate(aggregation))
        db.logout()
        return res
    except Exception as e:
        logger.info(str(e))
        return False

def insert_one(username, pwd, database, collection, data, logger):
    try:
        db = getattr(client, database)
        db.authenticate(username, pwd)
        res = db[collection].insert_one(data)
        db.logout()
        return True
    except Exception as e:
        logger.info("Failed to insert in Mongo")
        logger.info(str(e))
        return False

def update_one(username, pwd, database, collection, condition, data, logger):
    try:
        db = getattr(client, database)
        db.authenticate(username, pwd)
        res = db[collection].update(condition, {"$set":data})
        db.logout()
        logger.info("Inserted Successfully")
        return True
    except Exception as e:
        logger.info("Failed to insert in Mongo")
        logger.info(str(e))
        return False

def update_many(username, pwd, database, collection, condition, data, logger):
    try:
        db = getattr(client, database)
        db.authenticate(username, pwd)
        res = db[collection].update_many(condition, {"$set":data})
        db.logout()
        logger.info("Inserted Successfully")
        return True
    except Exception as e:
        logger.info("Failed to insert in Mongo")
        logger.info(str(e))
        return False