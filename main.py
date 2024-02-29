import os 
import pprint 
import datetime 
from pymongo import MongoClient 
from dotenv import load_dotenv 
from bson.objectid import ObjectId 
load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]
client =MongoClient(MONGODB_URI)
db = client.bank
accounts_collection = db.accounts 
new_accounts= [
    {
        name:"adekunle tosin bidemi",
        account_type: "checkings",
        balance:52648710,

        
    },
    {
        name:" anekwe ifunnaya",
        account_type:"savings",
        balance:21458730,
    },
    {
        name:"khallamullah",
        account_type:"fixed_deposit",
        balance:25410,
    },
    {
        name:"ada lovely lace",
        account_type:"savings",
        balance:5879410,
    },
    {
        name:"bashiru qaudri",
        account_type:"savings",
        balance:5648790,
    },
    {
        name:" bashiru musa adekunle ayinla",
        account_type:"current",
        balance:9875568983,
    },
    {
        name:"bashiru sofiyat",
        account_type:"current",
        balance:712540,
    },
    {
        name:"bashiru ibrahim ojo",
        account_type:"savings",
        balance:248782,
    },g

]
result = accounts_collection.insert_one(new_accounts)
document_ids = result.inserted_ids 
print(f"_id: of the inserted documents:{document_ids}")
print("# of document inserted:" + str(len(document_ids)))
print()
client.close()