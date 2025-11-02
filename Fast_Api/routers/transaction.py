# from fastapi import APIRouter
# import pymongo
# from pymongo.errors import ConnectionFailure
# import os

# router = APIRouter()


# MONGO_URI = f"mongodb://admin:admin123@202.92.6.165:27017/"
# DB_NAME = "budgetDB"
# COLLECTION_NAME = "budget"

# client = pymongo.MongoClient(MONGO_URI)
# db = client[DB_NAME]
# collection = db[COLLECTION_NAME]
# try:
#     client.admin.command('ping')
#     print("Connected to MongoDB")
# except ConnectionFailure:
#     print("Failed to connect to MongoDB")

# @router.post("/transactions/input")
# async def input():
#     new_budget = { 
#         "date": "11/10/2025", 
#         "category": "expense", 
#         "money": 50000 ,
#         "description": "Hôm nay đi ăn phở hết 50k"
#     }
    
#     insert_result = collection.insert_one(new_budget)
#     print(f"\n🎉 Đã chèn tài liệu với ID: {insert_result.inserted_id}")


from fastapi import APIRouter
from .db import db

router = APIRouter()

@router.post("/input")
async def input_transaction():
    new_budget = { 
        "date": "11/10/2025", 
        "category": "expo", 
        "money": 20000,
        "description": "Hôm nay đi ăn phở hết 20k"
    }

    result = db["budget"].insert_one(new_budget)
    print(f"🎉 Đã chèn tài liệu với ID: {result.inserted_id}")
    return {"message": "Insert success", "_id": str(result.inserted_id)}
