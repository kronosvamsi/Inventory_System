"""   -- Categories Service --
** Its a service class for CRUD operations at categories endpoint

"""
from models.categories import Category
from sqlalchemy import select
from schemas.category_schema import CategoryResponse

class CategoryService():
    count = 0
    
    def __init__(self):
        CategoryService.count+=1
    
    def create_category(self,**kwargs):
        new_category = kwargs["input_category"]
        session = kwargs["session"]
        db_record = Category(**new_category.model_dump())
        session.add(db_record)
        session.commit()
        return new_category
    
    def read_categories(self, session):
        db_records = session.scalars(select(Category)).all()
        response = [CategoryResponse.model_validate(record) for record in db_records]
        return response
        
    def read_categorybyId(self,**kwargs):
        id = kwargs['id']
        session = kwargs['session']
        db_record = session.scalars(select(Category).filter_by(id=id)).first()
        return CategoryResponse.model_validate(db_record)
        