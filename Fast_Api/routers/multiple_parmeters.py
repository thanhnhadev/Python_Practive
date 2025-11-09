# Body - Multiple Parameters
from fastapi import APIRouter, Query, Path
from pydantic import BaseModel
router = APIRouter()

class Item(BaseModel):
    name: str
    decriptipn: str | None = None
    price: float
    tax: float| None = None

@router.post("/items")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@router.put("/items/{item_id}")
async def create_item_with_put(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

@router.get("/items")
async def read_items(
    q: str
    | None = Query(
        None,
        min_length=3,
        max_length=10,
        title="Sample query string",
        description="This is a sample query string.",
        alias="item-query",
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@router.get("/items_hidden")
async def hidden_query_route(
    hidden_query: str | None = Query(None, include_in_schema=False)
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    return {"hidden_query": "Not found"}

@router.get("/items_validation/{item_id}")
async def read_items_validation(
    *,
    item_id: int = Path(..., title="The ID of the item to get", gt=10, le=100),
    q: str = "hello",
    size: float = Query(..., gt=0, lt=7.75)
):
    results = {"item_id": item_id, "size": size}
    if q:
        results.update({"q": q})
    return results