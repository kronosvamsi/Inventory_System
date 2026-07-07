'''
 ---- Inventory management System - Version:1.0 -----------
 
 '''

from fastapi import FastAPI,Depends
from routes import products,categories,users
from db.database import get_session
from schemas.inventory_schema import ReceiveStockRequest
from services.inventory_service import InventoryService

app = FastAPI()

""" Routers """
app.include_router(products.router)
app.include_router(categories.router)
app.include_router(users.router)

@app.get("/")
def home():
    return {"message" : "Hello to Inventory backend"} 

@app.post("/inventory")
def receive_stock(request:ReceiveStockRequest,product_id:int, db = Depends(get_session)):
    service = InventoryService()
    result = service.recieve_stock(db,product_id,request)
    return {"message":result}
