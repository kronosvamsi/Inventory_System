from fastapi import APIRouter, Depends
from db.database import get_session
from schemas.purchase_schema import PurchaseOrderRequest
from services.purchase_service import PurchaseService

router = APIRouter(
    prefix="/purchase",
    tags = ["purchases"],
    dependencies= []
)

@router.post("/order")
def purchase_order(request:PurchaseOrderRequest, db = Depends(get_session)):
    service = PurchaseService()
    service.create_purchase_order(db,request)
    pass