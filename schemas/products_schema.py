from pydantic import BaseModel,ConfigDict

class ProductInput(BaseModel):
    id:int
    name:str
    category_id : int
    sku:str
    quantity:int
    price:float

class ProductUpdate(BaseModel):
    name:str
    quantity:int
    price:float

class ProductResponse(BaseModel):
    id:int
    name:str
    sku:str
    quantity:int
    price:float
    
    model_config = ConfigDict(from_attributes = True) 