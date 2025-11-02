
from fastapi import APIRouter, Query, Path


router = APIRouter()
@router.get("/item_validation/{item_id}")
async def read_item_validation(
    *,
    item_id: int=Path(..., title="the id of the item to get",gt=10, le=100),
    q:str= "hello",
    size:float=Query(...,gt=0, lt=7.75)):
    results ={"item_id":item_id,"size":size}
    if q:
        results.update({"q":q})
    return results