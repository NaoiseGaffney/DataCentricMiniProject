
import os
import pymongo

from dotenv import load_dotenv
from pathlib import Path
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "TestMDB"
COLLECTION_NAME = "Names"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

""" new_doc = {"first": "Douglas", "last": "Adams", "dob": "11/03/1952", "hair_colour": "grey", "occupation": "writer", "nationality": "English"}
coll.insert(new_doc)
 """
""" new_docs = [{"first": "Terry", "last": "Pratchett", "dob": "28/04/1948", "gender": "m",
            "hair_colour": "not much", "occupation": "writer", "nationality": "English"}, {"first": "George", "last": "RR Martin", "dob": "20/09/1948", "hair_colour": "white", "occupation": "writer", "nationality": "American"}]
coll.insert_many(new_docs)
 """

documents = coll.find({"first": "douglas"})
# coll.remove({"first": "douglas"})
coll.update({"nationality": "american"}, {"$set": {"hair_colour": "purple"}})
coll.update({"nationality": "american"}, {"$set": {"hair_colour": "purple"}})

documents = coll.find()

for doc in documents:
    print(doc)


"""client = pymongo.MongoClient(
    "mongodb+srv://mdb_c_root:mdb_c_rootJam3s0n8@mdbcluster-vhvci.mongodb.net/TestMDB?retryWrites=true&w=majority")
db = client.testTestMDB
"""

"""
pip3 install pymongo
pip3 install python-dotenv
pip3 install dnspython
"""
