import pymongo
from robot.libraries.BuiltIn import BuiltIn

def InsertOne(con,data):
    try:
        try:
            db=pymongo.MongoClient(con["connection"])[con["database"]][con["collection"]]
        except KeyError:
            db=pymongo.MongoClient("mongodb://"+con["username"]+":"+con["password"]+"@"+con["host"]+":"+con["port"])[con["database"]][con["collection"]]

        db.insert_one(data).inserted_id
        return "INSERTED SUCCESS"
    except Exception as e:
        BuiltIn().log_to_console(e)
        return "INSERTED ERROR"