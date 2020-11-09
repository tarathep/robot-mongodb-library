import pymongo

def InsertOne(con,data):
    try:
        db=pymongo.MongoClient("mongodb://"+con["username"]+":"+con["password"]+"@"+con["host"]+":"+con["port"])[con["database"]][con["collection"]]
        db.insert_one(data).inserted_id
        return "INSERTED SUCCESS"
    except:
        return "INSERTED ERROR"