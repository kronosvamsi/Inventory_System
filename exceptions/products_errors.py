from fastapi import Request
from fastapi.responses import JSONResponse

class ProductNotFoundError(Exception):
    def __init__(self, message:str, product_id:int):
        super().__init__(message)
        self.message = message
        self.product_id = product_id

class NegativeQuantityError(Exception):
    def __init__(self, message:str, quantity :int):
        self.message  = message
        self.quantity = quantity
        super().__init__(message)

class NewQuantityError(Exception):
    def __init__(self, message:str, quantity :int):
        self.message  = message
        self.quantity = quantity
        super().__init__(message)


def negative_quantity_handler(request:Request, exc:NegativeQuantityError):
    return JSONResponse(
        status_code=400,
        content = {
            "error":"Negative_Quantity", 
            "msg":exc.message ,
            "quantity":exc.quantity
            }
        )

def new_quantity_handler(request:Request, exc:NewQuantityError):
    return JSONResponse(
        status_code=400,
        content = {
            "error":"New_Quantity_Error", 
            "msg":exc.message ,
            "quantity":exc.quantity
            }
        )
    

async def product_not_found_handler(request:Request, exc:ProductNotFoundError):
    return JSONResponse( 
        status_code= 404 ,
        content = {
            "error":"PRODUCT_NOT_FOUND",
            "msg":exc.message, 
            "product_id":exc.product_id
            }
) 

product_handlers = {
    ProductNotFoundError : product_not_found_handler,
    NegativeQuantityError : negative_quantity_handler,
    NewQuantityError : new_quantity_handler
}