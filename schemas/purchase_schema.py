from pydantic import BaseModel


class PurchaseOrderRequest(BaseModel):
    supplier_id:int
    product_id:int
    quantity:int

