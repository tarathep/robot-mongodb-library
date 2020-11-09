import pymongo
from pymongo import database
from bson.objectid import ObjectId
from pymongo.message import query

def InsertOne(con,data):
    try:
        db=pymongo.MongoClient("mongodb://"+con["username"]+":"+con["password"]+"@"+con["host"]+":"+con["port"])[con["database"]][con["collection"]]
        db.insert_one(data).inserted_id
        return "INSERTED SUCCESS"
    except:
        return "INSERTED ERROR"

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
        if db.delete_one({"_id":ObjectId(id)}).deleted_count != 0:return "DELETED SUCCESS"
        return "DATA NOT FOUND"
    except:
        return "DELETED ERROR"


def FindOneByID(con,id):
    try:
        db=pymongo.MongoClient("mongodb://"+con["username"]+":"+con["password"]+"@"+con["host"]+":"+con["port"])[con["database"]][con["collection"]]
        query = db.find_one({"_id":ObjectId(id)})
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

def Update(con,id,data):
    try:
        db=pymongo.MongoClient("mongodb://"+con["username"]+":"+con["password"]+"@"+con["host"]+":"+con["port"])[con["database"]][con["collection"]] 
        if db.update_one({"_id":ObjectId(id)},{ "$set": data}).modified_count !=0:
            return "UPDATED SUCCESS"
        return "DATA NOT FOUND"
    except:
        return "UPDATED ERROR"
