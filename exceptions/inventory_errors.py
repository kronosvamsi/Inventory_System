from fastapi import Request
from fastapi.responses import JSONResponse

class OutOfStockError(Exception):
    def __init__(self, message:str, available_quantity:int, required_quantity:int):
        super().__init__(message)
        self.message = message
        self.available = available_quantity
        self.required = required_quantity

class InventoryNotFoundError(Exception):
    def __init__(self, message:str, product_id:int):
        self.message = message
        self.product_id = product_id
        super.__init__(message)
    

async def out_of_stock_handler(request:Request, exc:OutOfStockError):
    return JSONResponse(
        status_code=400,
        content ={"error":"STOCK_EMPTY" ,"msg":f"{exc.message}", "availableQuantity":exc.available, "requiredQuantity":exc.required}
    )
async def inventory_not_found_handler(request:Request, exc:InventoryNotFoundError):
    return JSONResponse(
        status_code=404,
        content = {"error":"INVENTORY_404", "msg":exc.message,"product_id":exc.product_id}
    )

inventory_handlers = {

OutOfStockError : out_of_stock_handler,
InventoryNotFoundError : inventory_not_found_handler

}