""" Sale Service """

from sqlalchemy.orm import Session
from sqlalchemy import select
from models.sales_order import SalesOrder
from models.order_status import StatusType
from models.customer import Customer
from models.products import Product
from schemas.inventory_schema import SellStockRequest
from services.inventory_service import InventoryService


class SaleService():
   
    @staticmethod
    def create_sale_order(db , sale_data):
        customer = db.execute(select(Customer).where(Customer.id == sale_data.customer_id))
        if not customer :
            raise Exception(f"Customer with id {sale_data.customer_id} not found")
       
        product =  db.execute(select(Product).where(Product.id == sale_data.product_id))
        if not product:
            raise Exception(f"The Product with id {sale_data.product_id} not found")
        
        sale_order = SalesOrder(
            customer_id = sale_data.customer_id,
            product_id = sale_data.product_id,
            quantity = sale_data.quantity,
            status = StatusType.PENDING
            
        )

        db.add(sale_order)
        db.flush()
        db.commit()
        db.refresh(sale_order)

        return sale_order
    
    @staticmethod
    def approve_sale_order(db , sale_order_id):
        sale_order = db.execute(select(SalesOrder).where(SalesOrder.id == sale_order_id))
        if sale_order.status != StatusType.PENDING:
            raise Exception(f"The sale order with id {sale_order_id} is Invalid")
        
        sale_order.status = StatusType.APPROVED
        db.commit()
        db.refresh(sale_order)

        return sale_order
    
    @staticmethod
    def send_sale_order(db , sale_order_id):
        sale_order = db.execute(select(SalesOrder).where(SalesOrder.id == sale_order_id))
        if sale_order.status != StatusType.APPROVED:
            raise Exception(f"The sale order with id {sale_order_id} is Invalid")
        
        stock_request = SellStockRequest(
            product_id = sale_order.product_id,
            quantity = sale_order.quantity,
            reference_type = "SALE ORDER",
            reference_id = sale_order.product_id
        )

        InventoryService.sell_stock(db,stock_request)

        sale_order.status = StatusType.SHIPPED
        db.commit()
        db.refresh(sale_order)

        return sale_order