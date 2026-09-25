"""   -- Products Service -- 
** Its a service class for CRUD operations at products endpoint

"""
from sqlalchemy import select
from sqlalchemy.orm import Session

from models.products import Product
from models.inventory import Inventory

from schemas.products_schema import (
    ProductUpdate, 
    ProductCreate
)

class ProductService():
    
    @staticmethod
    def create_product(db:Session, product_data:ProductCreate):
        ## check whether SKU alrady exists
        existing_product = db.scalar(
            select(Product).where(
                Product.sku == product_data.sku
            
            )
        )
        
        if existing_product :
            raise ValueError(
                f"Product with SKU {product_data.sku} already exists"
            )
        
         # Create Product
        product = Product(
            name=product_data.name,
            sku=product_data.sku,
            category_id=product_data.category_id,
            price=product_data.price,
        )
        
        db.add(product)
        
        # Flush so PostgreSQL generates product.id
        db.flush()

        # Create Inventory record for this product
        inventory = Inventory(
            product_id=product.id,
            quantity_available=product_data.initial_quantity,
            reorder_level=product_data.reorder_level,
        )

        db.add(inventory)

        db.commit()

        db.refresh(product)
        
        return product
    
    @staticmethod
    def read_products(db : Session):
        products = db.scalars(
            select(Product).order_by(Product.id)
        ).all()
        # print("db records ",db_records )
        
        return products
    
    @staticmethod
    def read_product_byid(db:Session , product_id :int):
        product = db.scalar( 
            select(Product).where(
                Product.id == product_id
            )
        )
        if not product:
            raise ValueError(
                f" Product with id {product_id} not found"
            )
        return product
    
    @staticmethod  
    def update_product_byid(db : Session, product_id : int , product_data : ProductUpdate):
        product = db.scalar(
            select(Product).where(
                Product.id == product_id
            )
        )
        if not product:
            raise ValueError(
                f"Product with id {product_id} not found"
            )
        update_data = product_data.model_dump(
            exclude_unset=True
        )
        for field, value in update_data.items():
            if field == "reorder_level":
                product.inventory.reorder_level = value
            else:
                setattr(product, field, value)
        
        db.commit()
        
        db.refresh(product)

        return product
    
    @staticmethod
    def delete_product_byid(db : Session, product_id : int):
        product = db.scalar(
            select(Product).where(
                Product.id == product_id
            )
        )
        if not product:
            raise ValueError(
                f" Product with id {product_id} not found"
            )
        db.delete(product)
        db.commit()
        
        return {
            "message" : f"Product {product_id} deleted successfully"
        }
    
    