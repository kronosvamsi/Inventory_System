""" Inventory process """

from sqlalchemy import select
from models.inventory import Inventory
from models.instock import InventoryTransaction
from models.instock import TransactionType
from models.products import Product
from exceptions import OutOfStockError

class InventoryService():

    def __init__(self):
        pass

    def recieve_stock(self, db, product_id, request):
        product = db.scalars(select(Product).where(Product.id == product_id)).first()
        if product is None:
            raise Exception("Product doesn't exist")
        
        stock_record = db.scalars(select(Inventory).filter_by(product_id = product_id)).first()
        recieved_quantity = request.quantity
        stock_record.quantity_available += recieved_quantity
        
        transaction = InventoryTransaction(product_id = product.id,
                                           quantity = recieved_quantity,transaction_type = TransactionType.PURCHASE,
                                           reference_type = request.reference_type,reference_id = request.reference_id)
        
        db.add(transaction)
        db.commit()
        db.refresh(stock_record)
        return stock_record
    
    def sell_stock(self,db, request):
        product = db.scalars(select(Product).where(Product.id == request.product_id))
        if product is None:
            raise Exception("No Product found")
        
        inventory_record = db.scalars(select(Inventory).filter_by(product_id = request.product_id)).first()
        available = inventory_record.quantity_available
        if available < request.quantity:
            raise OutOfStockError(message = "The request quantity is not available", available_quantity=available, required_quantity=request.quantity)
        
        inventory_record.quantity_available -= request.quantity
        
        transaction = InventoryTransaction(
            product_id = product.id,  quantity = request.quantity,
            transaction_type = TransactionType.SALE, reference_type = request.reference_type,
            reference_id = request.reference_id
        )
        
        db.add(transaction)
        db.commit()
        db.refresh(inventory_record)

    
    def adjust_stock(self):
        pass


