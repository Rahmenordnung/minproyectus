import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = 'MyTestDb'
COLLECTION_NAME = "MyTestDb"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print('MOngo is here conneccted')
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print ('Could not connect to Mongo DB: %s') % e
        
conn = mongo_connect(MONGODB_URI)

coll= conn[DBS_NAME][COLLECTION_NAME]


documents= coll.update_one({'nationality': 'Usaien'}, {'$set': {'hair_colour': 'maroon'}})

documents = coll.find ({'nationality': 'Usaien'})

for doc in documents:
    print(doc)
    
   