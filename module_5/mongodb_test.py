import pymongo
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.nie00.mongodb.net/pytech?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.students
print(" -- Pytech COllection List -- ")
print(db.list_collection_names)
