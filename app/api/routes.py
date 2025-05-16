from fastapi import APIRouter, HTTPException
from app.schemas.item import Item, ItemCreate
from typing import List
import uuid

router = APIRouter(prefix="/items", tags=["items"])

# In-memory database for demonstration
items_db = {}

@router.get("", response_model=List[Item])
async def get_items():
    return list(items_db.values())

@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: str):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

@router.post("", response_model=Item, status_code=201)
async def create_item(item: ItemCreate):
    item_id = str(uuid.uuid4())
    new_item = Item(id=item_id, **item.dict())
    items_db[item_id] = new_item
    return new_item

@router.delete("/{item_id}", status_code=204)
async def delete_item(item_id: str):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return None 