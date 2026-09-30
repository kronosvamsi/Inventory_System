""" Purchase Service """
from sqlalchemy import select
from sqlalchemy.orm import Session
from models import Supplier, PurchaseOrder, Product
from schemas.purchase_schema import PurchaseOrder
from schemas.inventory_schema import ReceiveStockRequest
from models.order_status import StatusType
from services.inventory_service import InventoryService


class PurchaseService():
    
    def __init__(self):
        pass

    def create_purchase_order(self,db,request):
        supplier = db.execute(select(Supplier).where(Supplier.id == request.supplier_id)).first()
        if supplier is None:
            raise Exception("NO supplier found")
        product = db.execute(select(Product).where(Product.id == request.product_id)).first()
        if product is None:
            raise Exception("No Product found")
        purchase_order = PurchaseOrder(
            supplier_id = request.supplier_id, product_id = request.product_id,
            quantity = request.quantity, status = StatusType.PENDING
        )
        # print(purchase_order)
        
        db.add(purchase_order)
        db.commit()

        return purchase_order
    
    def approve_purchase_order(purchase_order_id:int, db:Session):
        purchase_order = db.execute(select(PurchaseOrder).where(PurchaseOrder.id == purchase_order_id )).first()
        if purchase_order.status != StatusType.PENDING:
            raise Exception( f"An Invalid Purchase Order {purchase_order.status}")
        
        purchase_order.status = StatusType.APPROVED
        db.commit()
        db.refresh(purchase_order)
        return purchase_order

    def receive_purchase_order(purchase_order_id:int , db:Session):
        purchase_order = db.execute(select(PurchaseOrder).where(PurchaseOrder.id == purchase_order_id )).first()
        if purchase_order.status != StatusType.APPROVED:
            raise Exception(f"An Invalid Purchase order status {purchase_order.status} ")
        
        receivestock_request = ReceiveStockRequest(
            product_id = purchase_order.product_id, 
            quantity = purchase_order.quantity, 
            reference_type = "PURCHASE_ORDER", 
            reference_id = purchase_order.id
        )
        
        InventoryService.receive_stock(db,receivestock_request)

        purchase_order.status = StatusType.RECEIVED

        db.commit()
        db.refresh(purchase_order)
        return purchase_order

