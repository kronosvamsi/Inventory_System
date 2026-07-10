""" Inventory process """

from sqlalchemy import select
from models.inventory import Inventory
from models.instock import InventoryTransaction
from models.instock import TransactionType
from models.products import Product
from exceptions import (
    OutOfStockError, 
    ProductNotFoundError,
    NegativeQuantityError, 
    db_exc_handler
)


class InventoryService():

    def __init__(self):
        pass
    
    def _get_product(self, db, product_id):
        record =  db.scalars(select(Product).where(Product.id == product_id)).first()
        if record is None:
            raise ProductNotFoundError( message = "The Product not found",product_id = product_id)
        return record
    
    
    def _get_inventory(self,db,product_id):
        return db.scalars(select(Inventory).filter_by(product_id = product_id)).first()
    
    
    def _validate_request_quantity(self, quantity):
        if quantity <= 0:
            raise  NegativeQuantityError( message = "Quantity should be positive and greater than Zero",quantity= quantity)
    
    @db_exc_handler
    def receive_stock(self, db, request):
        self._validate_request_quantity(request.quantity)
        product = self._get_product(db,request.product_id)
        stock_record = self._get_inventory(db, request.product_id)
        received_quantity = request.quantity
        stock_record.quantity_available += received_quantity
        
        transaction = InventoryTransaction(product_id = product.id,
                                           quantity = received_quantity,transaction_type = TransactionType.PURCHASE,
                                           reference_type = request.reference_type,reference_id = request.reference_id)
        
        db.add(transaction)
        db.commit()
        db.refresh(stock_record)
        return stock_record
    
    @db_exc_handler
    def sell_stock(self,db, request):
        self._validate_request_quantity(request.quantity)
        product = self._get_product(db, request.product_id)
        inventory_record = self._get_inventory(db,request.product_id)
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
        return inventory_record

    @db_exc_handler
    def adjust_stock(self,db, request):
        self._validate_request_quantity(request.new_quantity)
        product = self._get_product(db, request.product_id)
        inventory_record = self._get_inventory(db, request.product_id)
        
        old_quantity = inventory_record.quantity_available
        difference = request.new_quantity - old_quantity
        inventory_record.quantity_available =  request.new_quantity 
        
        transaction = InventoryTransaction(product_id = product.id, quantity = difference,
          transaction_type = TransactionType.ADJUSTMENT, reference_type = request.reference_type, 
          reference_id = request.reference_id
        )
        
        db.add(transaction)
        db.commit()
        db.refresh(inventory_record)
        return inventory_record
        
