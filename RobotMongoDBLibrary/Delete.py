import pymongo
from bson.objectid import ObjectId

def DeleteOne(con,fillter):
    try:
        db=pymongo.MongoClient("mongodb://"+con["username"]+":"+con["password"]+"@"+con["host"]+":"+con["port"])[con["database"]][con["collection"]]
        if db.delete_one(fillter).deleted_count != 0:return "DELETED SUCCESS"
        return "DATA NOT FOUND"
    except:
        print("error insert database")
        return "DELETED ERROR"

def DeleteOneByID(con,id):
    try:
        db=pymongo.MongoClient("mongodb://"+con["username"]+":"+con["password"]+"@"+con["host"]+":"+con["port"])[con["database"]][con["collection"]]
        try:
            _id=ObjectId(id)
        except:
            _id= id
        if db.delete_one({"_id":_id}).deleted_count != 0:return "DELETED SUCCESS"
        return "DATA NOT FOUND"
    except:
        return "DELETED ERROR"