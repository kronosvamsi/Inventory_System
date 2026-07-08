'''
 ---- Inventory management System - Version:1.0 -----------
 
 '''

from fastapi import FastAPI
from routes import products,categories,users,inventory
from exceptions import all_exceptions_handlers


app = FastAPI()

""" Add  all custom exception handler to the main app """

# print("exc", all_exceptions_handlers)
for exc_class, exc_handler in all_exceptions_handlers.items():
    app.add_exception_handler(exc_class,exc_handler)

""" Routers """
app.include_router(products.router)
app.include_router(categories.router)
app.include_router(users.router)
app.include_router(inventory.router)

@app.get("/")
def home():
    return {"message" : "Hello to Inventory backend"} 


