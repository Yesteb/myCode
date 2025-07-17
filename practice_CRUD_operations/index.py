from pymongo import MongoClient

client = MongoClient("mongodb+srv://esteban474sanchez:Yesteb@cluster0.rpbnucr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["PracticePython"]
collection = db["crud_operations"]

students = [
    {"name": "Esteban", "age": 20, "city": "Quito"},
    {"name": "Roberto", "age": 20, "city": "Medellin"},
    {"name": "Maria", "age": 20, "city": "Puerto Rico"}]

# Insert multiple documents
result = collection.insert_many(students)

# insert a single document
single_student = {"name": "Ana", "age": 23, "city": "Barranquilla"}
result_single = collection.insert_one(single_student)

# Read 
#find one document
student = collection.find_one({"name": "Esteban"})

# Find all documents
all_students = collection.find({"age": {"$gt": 20}})

# Update
# Update one document
collection.update_one({"name": "Esteban"}, {"$set": {"age": 21}})

#update many documents
collection.update_many({"city": {"$gt": "Medellin"}}, {"$set": {"city": "Updated City"}})

#delete
# Delete one document
collection.delete_one({"name": "Juan"})

# Delete many documents
collection.delete_many({"age": {"$lt": 21}})



