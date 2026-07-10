from pydantic import BaseModel

class BaseStockRequest(BaseModel):
    product_id:int
    quantity:int

class ReceiveStockRequest(BaseStockRequest):
    reference_type : str | None = None
    reference_id :int | None = None

class SellStockRequest(BaseStockRequest):
    reference_type : str | None = None
    reference_id :int | None = None

class AdjustStockRequest(BaseStockRequest):
    reference_type:str | None = None
    reference_id:int | None = None
    reason:str

"""" Check fields inherited """
# print(ReceiveStockRequest.model_fields.keys())
# print(SellStockRequest.model_fields.keys())
# print(AdjustStockRequest.model_fields.keys())