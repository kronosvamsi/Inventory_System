'''
 ---- Inventory management System - Version:1.0 -----------
 
 '''

from fastapi import FastAPI
from routes import products

app = FastAPI()

""" Products Router """
app.include_router(products.router)

@app.get("/")
def home():
    return {"message" : "Hello to Inventory backend"} 