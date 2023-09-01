import pymongo
import json
import certifi

ca = certifi.where()






uri = "mongodb+srv://Nikhil09:<Nikhil09>@cluster0.zviugbc.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri, tlsCAFile=ca)

db = client["mynewdatabase"]

col = db["hnji"]

test = {
    "name":"nikhil",
    "age":21
}
col.insert_one(test)

