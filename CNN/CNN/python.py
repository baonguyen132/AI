from pymongo import MongoClient
from sympy.parsing.sympy_parser import null

client = MongoClient("mongodb://localhost:27017/")

db = client["school"]             # Tạo hoặc kết nối tới database
collection = db["student"]       # Tạo hoặc kết nối tới collection

# collection.insert_one({
#     "name": "U",
#     "age": 21,
#     "address": "U",
#     "dob": null ,
#     "gpa": 3
# })

for doc in collection.find():
    print(doc["_id"])