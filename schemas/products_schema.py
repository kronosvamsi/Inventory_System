from pydantic import BaseModel,ConfigDict,Field
from decimal import Decimal
from datetime import datetime

class ProductCreate(BaseModel):
    name:str  = Field(min_length= 1, max_length= 150)
    category_id : int
    sku:str = Field(min_length= 1, max_length= 50)
    price:Decimal = Field(gt = 0, max_digits=10, decimal_places=2)
    initial_quantity : int = Field(default= 0, ge= 0)
    reorder_level : int  = Field(default = 10, ge =0)

class ProductUpdate(BaseModel):
    name:str | None =  Field(default = None ,min_length= 1, max_length= 150)
    category_id : int | None = None
    price:Decimal | None = Field(default= None, gt=0, max_digits=10, decimal_places=2)
    reorder_level : int | None = Field(default = None, ge = 0)

class ProductResponse(BaseModel):
    id:int
    name:str
    sku:str
    category_id :int
    price:Decimal
    created_at : datetime
    
    model_config = ConfigDict(from_attributes = True) 

class ProductDetailResponse(BaseModel):
    id: int
    name: str
    sku: str
    category_id: int
    price: Decimal
    created_at: datetime
    quantity_available: int
    reorder_level: int

    model_config = ConfigDict(from_attributes=True)