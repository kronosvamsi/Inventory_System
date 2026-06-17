from pydantic import BaseModel

class ProductInput(BaseModel):
    id:int
    name:str
    sku:str
    quantity:int
    price:float

class ProductUpdate(BaseModel):
    name:str
    quantity:int
    price:float
