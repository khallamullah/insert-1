import os
import pprint
import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv

load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]
client = MongoClient(MONGODB_URI)

def callback(
    session,
    transfer_id: None,
    account_id_sender: None,
    account_id_receiver: None,
    transfer_amount: None,
):
    accounts_collection = session.client.bank.accounts
    transfers_collection = session.client.bank.transfers

    transfer = {
        "transfer_id": transfer_id,
        "to_account": account_id_receiver,
        "from_account": account_id_sender,
        "amount": {"$numberDecimal": transfer_amount},
    }

    accounts_collection.update_one(
        {"account_id": account_id_sender},
        {"$inc": {"balance": -transfer_amount}, "$push": {"transfer complete": transfer_id}},
        session=session,
    )

    accounts_collection.update_one(
        {"account_id": account_id_receiver},
        {"$inc": {"balance": transfer_amount}, "$push": {"transfer complete": transfer_id}},
        session=session,
    )

    transfers_collection.insert_one(transfer, session=session)
    print("transaction successful")


def callback_wrapper(s):
    callback(
        s,
        transfer_id=00001,
        account_id_sender=8139383392,
        account_id_receiver=2270022898,
        transfer_amount=80000,
    )


with client.start_session() as session:
    session.with_transaction(callback_wrapper)

print()
client.close()
