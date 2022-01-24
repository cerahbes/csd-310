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


john = { "first_name": "John", "last_name": "Doe", "student_id": "1010"}
john_student_id = collection.insert_one(john).inserted_id

print("-- INSERT STATEMENTS --")
print("Inserted student record", john["first_name"], john["last_name"], "into the students collection with document_id ", john_student_id)
print()

doc = collection.find_one({"student_id": "1010"})
 
print("-- DISPLAYING STUDENT DOCUMENT", doc["student_id"], "--")
print("Student ID: ",doc["student_id"])
print("First Name: ",doc["first_name"])
print("Last Name: ",doc["last_name"])
print()

deadjohn = collection.delete_one({"student_id": "1010"})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in collection.find({}, { "student_id": 1, "first_name": 1, "last_name": 1}):
 print("Student ID:", doc["student_id"])
 print("First Name:", doc["first_name"])
 print("Last Name:", doc["last_name"])
 print()