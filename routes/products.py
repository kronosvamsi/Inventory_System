""" -- Products Routes -- """

from fastapi.routing import APIRouter
from fastapi import Depends,status
from typing import Annotated
from schemas.products_schema import (
    ProductCreate,
    ProductResponse,
    ProductUpdate
)
from db.database import get_session, SessionLocal
from services.products_service import ProductService
# from sqlalchemy import select
# from models.products import Product


router = APIRouter(
    prefix = "/products",
    tags = ["products"],
    dependencies = [] 
)


@router.get(
    "/", 
    response_model= list[ProductResponse]
)
def get_products(db:Annotated[SessionLocal, Depends(get_session)]):
    return ProductService.read_products(db)



@router.post(
    "/", 
    response_model = ProductResponse , 
    status_code = status.HTTP_201_CREATED
    )
def new_product(product_data:ProductCreate,db:Annotated[SessionLocal, Depends(get_session)]):
    return ProductService.create_product(db, product_data)



@router.get(
    "/{id}", 
    response_model= ProductResponse
    )
def get_product(db : Annotated[SessionLocal, Depends(get_session)], id:int):
    return ProductService.read_product_byid(db, id)


@router.patch(
    "/{id}", 
    response_model = ProductResponse
    )
def update_product(id:int, product_data:ProductUpdate, db:Annotated[SessionLocal, Depends(get_session)]):
    return ProductService.update_product_byid(db,id,product_data)


@router.delete(
    "/{id}"
    )
def delete_product(id:int , db:Annotated[SessionLocal, Depends(get_session)]):
    return  ProductService.delete_product_byid(db,id)

