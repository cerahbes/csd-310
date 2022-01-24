import pymongo
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.nie00.mongodb.net/pytech?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech
collection = db.students

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in collection.find({}, { "student_id": 1, "first_name": 1, "last_name": 1}):
 print("Student ID:", doc["student_id"])
 print("First Name:", doc["first_name"])
 print("Last Name:", doc["last_name"])
 print()
 
doc = collection.find_one({"student_id": "1008"})
 
print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("Student ID: ",doc["student_id"])
print("First Name: ",doc["first_name"])
print("Last Name: ",doc["last_name"])