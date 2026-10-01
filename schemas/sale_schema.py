from pydantic import BaseModel


class SaleData(BaseModel):
    customer_id : int 
    product_id : int
    quantity: int

class SaleDataResponse(BaseModel):
    id : int
    customer_id : int 
    product_id : int
    quantity: int
