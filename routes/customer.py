from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.customer import Customer
from schemas.customer_schema import(
    CustomerData,
    CustomerResponse
)
from db.database import get_session

router = APIRouter(
    prefix = "/customer",
    tags = ["Customers"],
    dependencies = []
)

@router.post("/", response_model = CustomerResponse)
def customer(customer_data:CustomerData, db:Session = Depends(get_session)):
    customer = Customer(
        name = customer_data.name,
        customer_type = customer_data.customer_type,
        address = customer_data.address,
        city = customer_data.city,
        state = customer_data.state,
        pincode = customer_data.pincode,
        email = customer_data.email,
        phone = customer_data.phone

    )

    db.add(customer)
    db.commit()
    db.refresh(customer)

    return customer

