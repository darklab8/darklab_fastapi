from fastapi import APIRouter

router = APIRouter()


@router.get("/items2/{item_id}")
async def read_item2(item_id: int):
    return {"item_id": item_id}
