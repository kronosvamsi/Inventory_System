""" Inventory API endpoints """

from fastapi import APIRouter, Depends
from db.database import get_session
from schemas.inventory_schema import ReceiveStockRequest
from services.inventory_service import InventoryService


router = APIRouter(
    prefix = "/inventory",
    tags=["inventories"],
    dependencies=[],
    
)

@router.post("/receive")
def receive_stock(request:ReceiveStockRequest,product_id:int, db = Depends(get_session)):
    service = InventoryService()
    result = service.recieve_stock(db,product_id,request)
    return {"message":result}