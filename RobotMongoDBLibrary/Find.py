import pymongo
from bson.objectid import ObjectId

def FindOneByID(con,id):
    try:
        db=pymongo.MongoClient("mongodb://"+con["username"]+":"+con["password"]+"@"+con["host"]+":"+con["port"])[con["database"]][con["collection"]]
        try:
            _id=ObjectId(id)
        except:
            _id=id
        query = db.find_one({"_id":_id})
        _id= str(query["_id"])
        query["_id"] = _id
        return query
    except:
        return "FOUND ERROR"

def Find(con,fillter):
    try:
        db=pymongo.MongoClient("mongodb://"+con["username"]+":"+con["password"]+"@"+con["host"]+":"+con["port"])[con["database"]][con["collection"]] 
        query = []
        for x in db.find(fillter):
            x["_id"]=str(x["_id"])
            query.append(x)
        return query
    except:
        return "FOUND ERROR"