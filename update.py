import os
import datetime
import pprint 
from pymongo import MongoClient 
from bson.objectid import ObjectId 
from dotenv import load_dotenv 
load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]
client= MongoClient(MONGODB_URI)
db= client.bank
accounts_collection = db.accounts 
filtered_by_id= {"_id": ObjectId("fdga8sdgsbgdf6bdf4h")}
add_to_balance= {"$inc":{"balance": 5820}}
print("searching for target document before upating......")
pprint.pprint(filtered_by_id)
result= accounts_collection.update_one(filtered_by_id,add_to_balance)
print("searching for target document after updating.....")
pprint.pprint(result)
print("document matched" + str(result.matched_count))
print("document updated" + str(result.modified_count))
print()
client.close()
