import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "mytestdb"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

# CRUD Operations:
# coll.insert({search string})
# coll.insert_many({search string})
# coll.find({search string})
# coll.update_one({search string})
# coll.update_many({search string})
# coll.remove({search string})

documents = coll.find()

for doc in documents:
    print(doc)