""" Purchase Service """
from sqlalchemy import select
from models import Supplier, PurchaseOrder, Product
from models.order_status import StatusType

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
        print(purchase_order)
        # db.add(purchase_order)
        # db.commit()
    