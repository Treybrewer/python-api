from pydantic import BaseModel

class ItemBase(BaseModel):

    item_class: int

class Item(ItemBase):
    area: float
    perimter: float
    compactness: float
    length: float
    width: float
    asymmetry: float
    groove: float
    class Config:
        orm_mode = True
