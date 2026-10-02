from pydantic import BaseModel, ConfigDict
from models.order_status import StatusType

class SaleData(BaseModel):
    customer_id : int 
    product_id : int
    quantity: int

class SaleDataResponse(BaseModel):
    id : int
    customer_id : int 
    product_id : int
    quantity: int
    status : StatusType

    model_config = ConfigDict(from_attributes = True)
