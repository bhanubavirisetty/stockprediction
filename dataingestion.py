from pymongo import MongoClient
from datafetch import fetch_data

# Insertion of Data into MongoDb
def insert_data_to_mongo(data, connection_string, db, collection):
    client = MongoClient(connection_string)
    db_name = client[db]
    collection_name = db_name[collection]

    # Insert all the Stock Data into MongoDB Atlas
    collection_name.insert_many(data.to_dict(orient="records"))

    # Documents Count inside the MongoDB
    query_count = collection_name.count_documents({})
    print(f"The total number of documents {query_count}")

# Delete all documents
def deleteAll(connection_string, db, collection):
    client = MongoClient(connection_string)
    db_name = client[db]
    collection_name = db_name[collection]

    # Delete all documents from the collection
    collection_name.delete_many({})

# MongoDB Atlas Connection Details
connection_string = "mongodb+srv://bnpavankumarbavirisetty1998:Cloud123@stock-data-cluster.f0cjt.mongodb.net/?retryWrites=true&w=majority&appName=stock-data-cluster"
db = "stockdb"
collection = "stockcollection"

if __name__ == "__main__":
    data = fetch_data()
    insert_data_to_mongo(data, connection_string, db, collection)
    #deleteAll(connection_string, db, collection)
