import os
import datetime 
import pprint 
from pymongo import MongoClient 
from bson.objectid import ObjectId 
from dotenv import load_dotenv 
load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]
client = MongoClient(MONGODB_URI)
db= client.bank
accounts_collection= db.accounts 
filtered_by_type ={"account_type": "savings"}
add_to_balance= {"$set": {"minimum_balance": 200}}
print("searching for target documents before modification.....")
pprint.pprint(accounts_collection.find_one(filtered_by_type))
result = accounts_collection.update_many(filtered_by_type, add_to_balance)
print("searching for target documents after modification......")
pprint.pprint(accounts_collection.find_one(filtered_by_type))
print("document matched" + str(result.matched_count))
print("document modified" + str(result.modified_count))
print()
client.close()