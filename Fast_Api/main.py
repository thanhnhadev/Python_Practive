from fastapi import FastAPI
from routers.db import connect_to_mongo, close_mongo_connection
from routers import transaction, ai_chat, test, query_parameter, numeric_validation, multiple_parmeters
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db_client():
    close_mongo_connection()

app.include_router(transaction.router, prefix="/transaction", tags=["Transaction"])
app.include_router(ai_chat.router, prefix="/chat", tags=["Open AI"])
app.include_router(test.router, tags=["Test"])

app.include_router(query_parameter.router, tags=["query paramete"])
app.include_router(numeric_validation.router, tags=["numeric validation"])
app.include_router(multiple_parmeters.router, tags=["multiple parmeters"])
