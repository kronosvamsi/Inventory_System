'''
 ---- Inventory management System - Version:1.0 -----------
 
 '''

from fastapi import FastAPI
from routes import products,categories

app = FastAPI()

""" Routers """
app.include_router(products.router)
app.include_router(categories.router)

@app.get("/")
def home():
    return {"message" : "Hello to Inventory backend"} 