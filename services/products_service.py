"""   -- Products Service -- 
** Its a service class for CRUD operations at products endpoint

"""
from models.products import Product
from models.inventory import Inventory
from sqlalchemy import select
from schemas.products_schema import ProductResponse

class ProductService():
    count = 0
    
    def __init__(self):
        ProductService.count+=1
    
    def create_product(self,**kwargs):
        session = kwargs['session']
        new_product = kwargs['new_product']
        
        product = Product(**new_product.model_dump())
        inventory = Inventory(product_id = product.id, quantity_available = product.quantity)
        
        session.add(product)
        session.add(inventory)
        session.commit()
        
        return new_product
    
    def read_products(self,session):
        db_records = session.scalars(select(Product)).all()
        # print("db records ",db_records )
        response = [ProductResponse.model_validate(product) for product in db_records]
        return response
    
    def read_product_byid(self):
        pass
    def update_product_byid(self):
        pass
    def delete_product_byid(self):
        pass
    
    