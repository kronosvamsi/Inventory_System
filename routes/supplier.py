from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.supplier import Supplier
from schemas.supplier_schema import SupplierData, SupplierResponse
from db.database import get_session

router = APIRouter(
    prefix="/supplier",
    tags = ["suppliers"],
    dependencies= []
)

@router.post("/",response_model= SupplierResponse)
def supplier( supplier_data : SupplierData,  db : Session = Depends(get_session)):
    supplier = Supplier(
        name = supplier_data.name,
        supplier_type  = supplier_data.supplier_type, 
        address  = supplier_data.address,
        city  =  supplier_data.city,
        state  = supplier_data.state,
        pincode  = supplier_data.pincode,
        email  = supplier_data.email,
        phone = supplier_data.phone
    )
    
    db.add(supplier)
    db.commit()
    db.refresh(supplier)

    return supplier