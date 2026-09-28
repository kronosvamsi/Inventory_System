"""   -- Categories Service --
** Its a service class for CRUD operations at categories endpoint

"""
from models.categories import Category
from sqlalchemy import select
from sqlalchemy.orm import Session
from schemas.category_schema import (
    CategoryCreate,
    CategoryUpdate
)

class CategoryService():
    
    @staticmethod
    def create_category(db:Session, category_data:CategoryCreate):
        
        category_item = db.scalar(select(Category).where(Category.name == category_data.name))
        
        if category_item :
            raise ValueError("The Category item is already exists !")
        
        category = Category(
            name = category_data.name, 
            description = category_data.description
            )
        db.add(category)

        db.flush()
        
        db.commit()

        db.refresh(category)

        return category
    
    @staticmethod
    def read_categories(db:Session):
        categories = db.scalars(
            select(Category).order_by(Category.id)
            ).all()
        
        return categories
    
    @staticmethod
    def read_categorybyId(db:Session, id:int):
        
        category = db.scalar(
            select(Category).where(
                Category.id == id
                )
            )
        if not category:
            raise ValueError(f"The Category by id {id} not found")

        return category
   
   
    @staticmethod
    def update_categorybyId(db:Session, id:int, update_category:CategoryUpdate):
        
        category = db.scalar(
            select(Category).where(
                Category.id == id
                )
            )
        if not category:
            raise ValueError(f"The Category by id {id} not found")
        
        update_data = update_category.model_dump()
        
        for field,val in update_data.items():
            setattr(category,field,val)
        
        db.commit()
        db.refresh(category)
        return category
    
    def delete_categorybyId(db:Session, id:int):
        
        category = db.scalar(
            select(Category).where(
                Category.id == id
                )
            
            )
        if not category :
            raise ValueError(f"The Category by id {id} not found")
        
        db.delete(category)
        db.commit()

        return {"message":f"The Category with id {id} deleted successfully"}
