import pymongo
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.nie00.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
students = db["students"]

docs = db.students.find({})

print("--DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in docs:
 print(doc)
 print()
 
doc = db.students.find_one({"student_id": "1008"})
 
print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("Student ID: ",doc["student_id"])
print("First Name: ",doc["first_name"])
print("Last Name: ",doc["last_name"])