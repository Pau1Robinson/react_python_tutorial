import os
from pymongo import MongoClient

COLLECTION_NAME = 'PFRM'
#manually added address actual app should use environmental variable
MONGO_URL = 'mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb'

class MongoRepository(object):
    def __init__(self):
        #os.environ.get('MONGO_URL')
        mongo_url = MONGO_URL
        self.db = MongoClient(mongo_url).PFRM
    
    def find_all(self, selector):
        return self.db.PFRM.find(selector)

    def find(self, selector):
        return self.db.PFRM.find_one(selector)

    def create(self, PFRM):
        return self.db.PFRM.insert_one(PFRM)

    def update(self, selector, PFRM):
        return self.db.PFRM.replace_one(selector, PFRM).modified_count

    def delete(self, selector):
        return self.db.PFRM.delete_one(selector).deleted_count
