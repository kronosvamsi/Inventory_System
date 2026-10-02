from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_session
from schemas.sale_schema import(
    SaleData,
    SaleDataResponse
)

from services.sale_service import SaleService

router = APIRouter(
    prefix = "/sales",
    tags = ["Sales"],
    dependencies = []
)

@router.post("/order", response_model = SaleDataResponse)
def sale_order( sale_data:SaleData , db :Session = Depends(get_session)):
    return SaleService.create_sale_order(db, sale_data)

@router.patch("/order/approve/{id}", response_model = SaleDataResponse)
def approve_order( id:int , db :Session = Depends(get_session)):
    return SaleService.approve_sale_order(db , id)


@router.patch("/order/send/{id}" , response_model= SaleDataResponse)
def send_order( id:int , db :Session = Depends(get_session)):
    return SaleService.send_sale_order(db , id)

@router.get("/order", response_model= list[SaleDataResponse])
def sale_order(db:Session = Depends(get_session)):
    return SaleService.get_sale_orders(db)