""" -- Categories Routes -- """

from fastapi.routing import APIRouter
from fastapi import Depends,status
from typing import Annotated
from schemas.category_schema import CategoryCreate, CategoryResponse, CategoryUpdate
from db.database import SessionLocal, get_session
from services.category_service import CategoryService


router = APIRouter(
    prefix = "/categories",
    tags = ["categories"],
    dependencies=[]
)

@router.post("/",

response_model = CategoryResponse,
status_code = status.HTTP_201_CREATED
)
def new_category(inputcategory:CategoryCreate, 
                 session:Annotated[SessionLocal, Depends(get_session)]
                 ):
    return  CategoryService.create_category(session, inputcategory)

@router.get("/",
response_model = list[CategoryResponse]

)
def get_categories(session:Annotated[SessionLocal, Depends(get_session)]):
    
    return  CategoryService.read_categories(session)

@router.get(
    "/{id}",
    response_model = CategoryResponse
)
def get_category(id:int, session:Annotated[SessionLocal, Depends(get_session)]):

    return CategoryService.read_categorybyId(session,id)

@router.patch(
    "/{id}",
    response_model = CategoryResponse
)
def update_category(id:int,
                    inputCategory:CategoryUpdate, 
                    session:Annotated[SessionLocal, Depends(get_session)]):
    
    return CategoryService.update_categorybyId(session, id, inputCategory)

@router.delete(
    "/{id}",
)
def delete_category(id:int,session:Annotated[SessionLocal, Depends(get_session)]):

    return  CategoryService.delete_categorybyId(session,id)

