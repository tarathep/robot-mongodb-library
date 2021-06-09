import pymongo
from bson.objectid import ObjectId
from robot.libraries.BuiltIn import BuiltIn

def Update(con,id,data):
    try:
        try:
            db=pymongo.MongoClient(con["connection"])[con["database"]][con["collection"]]
        except KeyError:
            db=pymongo.MongoClient("mongodb://"+con["username"]+":"+con["password"]+"@"+con["host"]+":"+con["port"])[con["database"]][con["collection"]]

        try:
            _id=ObjectId(id)
        except:
            _id=id
        if db.update_one({"_id":_id},{ "$set": data}).modified_count !=0:
            return "UPDATED SUCCESS"
        return "DATA NOT FOUND"
    except Exception as e:
        BuiltIn().log_to_console(e)
        return "UPDATED ERROR"