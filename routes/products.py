from fastapi.routing import APIRouter
from fastapi import Depends
from schemas.products_schema import ProductInput, ProductUpdate

router = APIRouter(
    prefix = "/products",
    tags = ["products,"],
    dependencies = [] or None
)

@router.get("/")
def get_products():
    return {"message":"Products"}

@router.post("/")
def new_product(inputProduct:ProductInput):
    # print(inputProduct)
    pass

@router.get("/{id}")
def get_product(id:int):
    return {"message":"Got product by Id"}

@router.patch("/{id}")
def update_product(id:int, new_update:ProductUpdate):
    return {"message":new_update.model_dump()}

@router.delete("/{id}")
def delete_product(id:int):
    return {"message":"Item deleted by Id"}

