from pydantic import BaseModel

class ReceiveStockRequest(BaseModel):
    quantity:int
    reference_type : str | None = None
    reference_id :str | None = None

class SellStockRequest(BaseModel):
    product_id:int
    quantity:int
    reference_type : str | None = None
    reference_id :str | None = None