from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: str = None
    price: float

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: str

    class Config:
        orm_mode = True 