from fastapi import APIRouter, Depends
from db.database import get_session
from schemas.purchase_schema import (
    PurchaseData, 
    PurchaseOrderResponse
)
from services.purchase_service import PurchaseService

router = APIRouter(
    prefix="/purchase",
    tags = ["purchases"],
    dependencies= []
)

@router.post("/order", response_model= PurchaseOrderResponse)
def purchase_order(request:PurchaseData, db = Depends(get_session)):
    return PurchaseService.create_purchase_order(db, request)


@router.patch("/order/approve/{id}" , response_model= PurchaseOrderResponse)
def approve_order(id:int , db = Depends(get_session)):
    return PurchaseService.approve_purchase_order(id, db)

@router.patch("/order/receive/{id}" , response_model= PurchaseOrderResponse)
def receive_order(id:int, db = Depends(get_session)):
    return PurchaseService.receive_purchase_order(id, db)

@router.get("/order", response_model= list[PurchaseOrderResponse])
def purchase_orders( db  = Depends(get_session)):
    return PurchaseService.get_purchase_orders(db)
