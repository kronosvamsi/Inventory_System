""" Inventory API endpoints """

from fastapi import APIRouter, Depends
from db.database import get_session
from schemas.inventory_schema import ReceiveStockRequest, SellStockRequest, AdjustStockRequest
from services.inventory_service import InventoryService


router = APIRouter(
    prefix = "/inventory",
    tags=["inventories"],
    dependencies=[],
    
)

@router.post("/receive")
def receive_stock(request:ReceiveStockRequest, db = Depends(get_session)):
    service = InventoryService()
    result = service.receive_stock(db,request)
    return {"message":result}

@router.post("/send")
def send_stock(request:SellStockRequest, db = Depends(get_session)):
    service = InventoryService()
    result = service.sell_stock(db, request)
    return {"message":result}

@router.post("/adjust")
def adjust_stock(request:AdjustStockRequest, db = Depends(get_session)):
    service = InventoryService()
    result = service.adjust_stock(db,request)
    return {"message":result}
