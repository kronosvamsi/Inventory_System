""" -- Products Routes -- """

from fastapi.routing import APIRouter
from fastapi import Depends
from typing import Annotated
from schemas.products_schema import ProductInput, ProductUpdate
from db.database import get_session, SessionLocal
from services.products_service import ProductService
# from sqlalchemy import select
# from models.products import Product


router = APIRouter(
    prefix = "/products",
    tags = ["products"],
    dependencies = [] 
)

@router.get("/")
def get_products(session:Annotated[SessionLocal, Depends(get_session)]):
    service = ProductService()
    response = service.read_products(session)
    return response

@router.post("/")
def new_product(inputProduct:ProductInput,session:Annotated[SessionLocal, Depends(get_session)]):
    service = ProductService()
    response = service.create_product(session = session, new_product = inputProduct)
    return response

@router.get("/{id}")
def get_product(id:int):
    return {"message":"Got product by Id"}

@router.patch("/{id}")
def update_product(id:int, new_update:ProductUpdate):
    return {"message":new_update.model_dump()}

@router.delete("/{id}")
def delete_product(id:int):
    return {"message":"Item deleted by Id"}

