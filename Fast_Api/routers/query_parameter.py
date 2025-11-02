
from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/items")
async def read_items(
    q: str | None = Query(None, min_length=3, 
                          max_length=10, 
                          title="sample query string", 
                          description="this is a sample query string", 
                          deprecated= True,
                          alias='item-query')):
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