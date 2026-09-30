from pydantic import BaseModel


class PurchaseOrder(BaseModel):
    id:int
    supplier_id:int
    product_id:int
    quantity:int

class PurchaseOrderResponse(BaseModel):
    id:int
    supplier_id:int
    product_id:int
    quantity:int
