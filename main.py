'''
 ---- Inventory management System - Version:1.0 -----------
 
 '''

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import products,categories,users,inventory,purchase, supplier, sales,customer
from exceptions import all_exceptions_handlers


app = FastAPI()

origins = [
    "http://localhost:5173",
     "http://127.0.0.1:5173",
]

### Cors Middleware ### 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


""" Add  all custom exception handler to the main app """

# print("exc", all_exceptions_handlers)
for exc_class, exc_handler in all_exceptions_handlers.items():
    app.add_exception_handler(exc_class,exc_handler)

""" Routers """
app.include_router(products.router , prefix = "/api")
app.include_router(categories.router , prefix = "/api")
app.include_router(users.router)
app.include_router(inventory.router)
app.include_router(purchase.router)
app.include_router(sales.router)
app.include_router(supplier.router)
app.include_router(customer.router)

@app.get("/")
def home():
    return {"message" : "Hello to Inventory backend"} 


