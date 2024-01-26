import pymongo
import os
from config import *

mongo = pymongo.MongoClient(DB_URL)

db = mongo[DB_NAME]
dbcol = db["user"]

#def addthumb(chat_id, file_id):
    #dbcol.update_one({"_id": chat_id}, {"$set": {"file_id": file_id}})


#def delthumb(chat_id):
    #dbcol.update_one({"_id": chat_id}, {"$set": {"file_id": None}})


def addcaption(chat_id, caption):
    dbcol.update({"_id": chat_id}, {"$set": {"caption": caption}})

def delcaption(chat_id):
    dbcol.update({"_id": chat_id}, {"$set": {"caption": None}})


def find(chat_id):
    id = {"_id": chat_id}
    x = dbcol.find(id)
    for i in x:
        file = i["file_id"]
        try:
            caption = i["caption"]
        except:
            caption = None
        return [file, caption]




