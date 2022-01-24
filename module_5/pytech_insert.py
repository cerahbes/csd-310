import pymongo
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.nie00.mongodb.net/pytech?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech
collection = db.students

thorin = { "first_name": "Thorin", "last_name": "Oakenshield", "student_id": "1007"}
bilbo = { "first_name": "Bilbo", "last_name": "Baggins", "student_id": "1008"}
frodo = { "first_name": "Frodo", "last_name": "Baggins", "student_id": "1009"}

thorin_student_id = collection.insert_one(thorin).inserted_id
bilbo_student_id = collection.insert_one(bilbo).inserted_id
frodo_student_id = collection.insert_one(frodo).inserted_id

print("-- INSERT STATEMENTS --")
print("Inserted student record", thorin["first_name"], thorin["last_name"], "into the students collection with document_id ", thorin_student_id)
print("Inserted student record", bilbo["first_name"], bilbo["last_name"], "into the students collection with document_id ", bilbo_student_id)
print("Inserted student record", frodo["first_name"], frodo["last_name"], "into the students collection with document_id ", frodo_student_id)