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
    NewQuantityError,
    InventoryNotFoundError,
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
        record  = db.scalars(select(Inventory).filter_by(product_id = product_id)).first()
        if record is None:
            raise InventoryNotFoundError(message = "No Inventory record found",product_id= product_id)
        return record
    
    def _validate_request_quantity(self, quantity):
        if quantity <= 0:
            raise  NegativeQuantityError( message = "Quantity should be positive and greater than Zero",quantity= quantity)
    
    def _validate_new_quantity(self,quantity):
        if quantity < 0:
            raise NewQuantityError(message = "New Quantity should be positive(greater or equal to zero)", quantity = quantity)
    
    
    def validate_and_get_inventory_record(self, db,request):
        self._validate_request_quantity(request.quantity)
        product = self._get_product(db,request.product_id)
        return  self._get_inventory(db, request.product_id)
    
    @staticmethod
    def increase_stock_and_transaction(inventory_record,request,db):
        inventory_record.quantity_available += request.quantity
        transaction = InventoryTransaction(product_id = request.product_id,
                                           quantity = request.quantity,transaction_type = TransactionType.PURCHASE,
                                           reference_type = request.reference_type,reference_id = request.reference_id)
        db.add(transaction)
    
    @staticmethod
    def decrease_stock_and_transaction(inventory_record, request, db):
        available = inventory_record.quantity_available
        if available < request.quantity:
            raise OutOfStockError(message = "The request quantity is not available", available_quantity=available, required_quantity=request.quantity)
        inventory_record.quantity_available -= request.quantity
        transaction = InventoryTransaction(
            product_id = request.product_id, quantity = request.quantity,
            transaction_type = TransactionType.SALE, reference_type = request.reference_type,
            reference_id = request.reference_id
        )
        db.add(transaction)
    
    @db_exc_handler
    def receive_stock(self, db, request):
        inventory_record = self.validate_and_get_inventory_record(db,request)
        self.increase_stock_and_transaction(inventory_record, request,db)
        db.commit()
        db.refresh(inventory_record)
        return inventory_record
    
    @db_exc_handler
    def sell_stock(self,db, request):
        inventory_record = self.validate_and_get_inventory_record(db,request)
        self.decrease_stock_and_transaction(inventory_record,request,db)
        db.commit()
        db.refresh(inventory_record)
        return inventory_record

    @db_exc_handler
    def adjust_stock(self,db, request):
        self._validate_new_quantity(request.new_quantity)
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
    
    @staticmethod  
    def get_inventory_items(db):
        inventory_items = db.execute(
            select(Inventory).order_by(Inventory.id)
            ).scalars().all()
        
        # print("items:",inventory_items)
        return inventory_items
        