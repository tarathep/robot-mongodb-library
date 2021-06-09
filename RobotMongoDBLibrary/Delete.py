import pymongo
from bson.objectid import ObjectId
from robot.libraries.BuiltIn import BuiltIn

def DeleteOne(con,fillter):
    try:
        try:
            db=pymongo.MongoClient(con["connection"])[con["database"]][con["collection"]]
        except KeyError:
            db=pymongo.MongoClient("mongodb://"+con["username"]+":"+con["password"]+"@"+con["host"]+":"+con["port"])[con["database"]][con["collection"]]
        
        if db.delete_one(fillter).deleted_count != 0:return "DELETED SUCCESS"
        return "DATA NOT FOUND"
    except Exception as e:
        BuiltIn().log_to_console(e)
        return "DELETED ERROR"

def DeleteOneByID(con,id):
    try:
        try:
            db=pymongo.MongoClient(con["connection"])[con["database"]][con["collection"]]
        except KeyError:
            db=pymongo.MongoClient("mongodb://"+con["username"]+":"+con["password"]+"@"+con["host"]+":"+con["port"])[con["database"]][con["collection"]]
        
        try:
            _id=ObjectId(id)
        except:
            _id= id
        if db.delete_one({"_id":_id}).deleted_count != 0:return "DELETED SUCCESS"
        return "DATA NOT FOUND"
    except Exception as e:
        BuiltIn().log_to_console(e)
        return "DELETED ERROR"