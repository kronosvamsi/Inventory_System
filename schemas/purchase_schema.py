from pydantic import BaseModel, ConfigDict


class PurchaseData(BaseModel):
    supplier_id:int
    product_id:int
    quantity:int

class PurchaseOrderResponse(BaseModel):
    id:int
    supplier_id:int
    product_id:int
    quantity:int

    model_config = ConfigDict(from_attributes = True)
