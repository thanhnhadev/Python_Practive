from enum import Enum
from fastapi import APIRouter
from typing import Optional
from pydantic import BaseModel
router = APIRouter()

@router.get("/")
async def base_get_route():
    return {"message": "Hello-World"}

@router.post("/")
async def post():
    return {"message":"hello from post route"}

@router.put("/")
async def put():
    return {"message":"hello from put route"}

@router.get("/users")
async def list_user():
    return {"message":"list user route"}

@router.get("/users/me")
async def get_current_user():
    return {"message":"this is the current user"}

@router.get("/users/{user_id}")
async def get_user(user_id:str):
    return {"user_id":user_id}

class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"

@router.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return{
            "food_name":food_name,
            "message":"you are healthy"
            }
    
    if food_name.value =='fruits':
        return {
            "food_name":food_name,
            "message":"you are still healthy, but like sweet things"
        }
    return {"food_name":food_name,"message":"i like chocolate milk"}

fake_items_db =[
    {"item_name":"Foo"},
    {"item_name":"Bar"},
    {"item_name":"Baz"}
    ]

@router.get("/items")
async def list_items(skip:int =0, limit:int=10):
    return fake_items_db[skip:skip+limit]

@router.get("/items/{item_id}")
async def get_item(item_id:str, sample_query_param:str, q:str|None= None, short: bool = False):
    item = {
            "item_id":item_id, 
            "sample_query_param":sample_query_param
            }
    if q:
        item.update({"q":q})
    if not short:
        item.update(
                {
                "description":"Lorem ipsum Lora"
                }
            )
    return item

@router.get("/users/{user_id}/items/{item_id}")
async def get_user_item(user_id:int, item_id:str,q:str | None= None, short: bool = False):
    item={
        "item_id": item_id,
        "owner_id":user_id
    }
    if q:
        item.update({
            "q":q
        })
    if not short:
        item.update(
                {
                "description":"Lorem ipsum Lora"
                }
            )
    return item

class Item(BaseModel):
    name: str
    description: Optional[str]= None
    price:str
    tax:float | None = None


@router.post("/items")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update(
            {"price_with_tax": price_with_tax}
            )
    return item_dict

@router.put("/items/{item_id}")
async def create_item_with_put(item_id:int, item: Item, q: str| None= None):
    result= {"item_id":item_id,**item.dict()}
    if q:
        result.update({"q":q})
    return result