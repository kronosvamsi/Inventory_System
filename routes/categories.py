""" -- Categories Routes -- """

from fastapi.routing import APIRouter
from fastapi import Depends
from typing import Annotated
from schemas.category_schema import CategoryInput, CategoryResponse, CategoryUpdate
from db.database import SessionLocal, get_session
from services.category_service import CategoryService


router = APIRouter(
    prefix = "/categories",
    tags = ["catgories"],
    dependencies=[]
)

@router.post("/")
def new_category(inputCategory:CategoryInput, 
                 session:Annotated[SessionLocal, Depends(get_session)]
                 ):
    
    service = CategoryService()
    response = service.create_category(input_category = inputCategory, session = session)
    return {
            "message":"A new category added",
            "response":response
            }

@router.get("/")
def get_categories(session:Annotated[SessionLocal, Depends(get_session)]):
    service = CategoryService()
    response = service.read_categories(session)
    return {
            "message":"A list of categories ",
            "response" : response
            }

@router.get("/{id}")
def get_category(id:int, session:Annotated[SessionLocal, Depends(get_session)]):
    service = CategoryService()
    response = service.read_categorybyId(id = id, session = session)
    return {
        "message":"A category by id",
        "response":response
        }

@router.patch("/{id}")
def update_category(id:int,
                    inputCategory:CategoryUpdate, 
                    session:Annotated[SessionLocal, Depends(get_session)]):
    service = CategoryService()
    response = service.update_categorybyId(id = id,input_category = inputCategory,session = session)
    return {
        "message":"A category update",
        "response":response
        }

@router.delete("/{id}")
def delete_category(id:int,session:Annotated[SessionLocal, Depends(get_session)]):
    service = CategoryService()
    service.delete_categorybyId(id = id, session = session)
    return {"message":"A Category deleted"}
