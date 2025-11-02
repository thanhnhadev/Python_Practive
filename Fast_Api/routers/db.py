# app/routers/db.py
import os
import pymongo
from pymongo.errors import ConnectionFailure

MONGO_URI = f"mongodb://admin:admin123@202.92.6.165:27017/"
DB_NAME = "budgetDB"
COLLECTION_NAME = "budget"

client = pymongo.MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def connect_to_mongo():
    global client, db
    try:
        client.admin.command("ping")
        print("✅ Connected to MongoDB")
    except ConnectionFailure as e:
        print(f"❌ MongoDB connection failed: {e}")

def close_mongo_connection():
    global client
    if client:
        client.close()
        print("🛑 MongoDB connection closed")


