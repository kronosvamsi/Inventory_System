from fastapi import Request
from fastapi.responses import JSONResponse

class OutOfStockError(Exception):
    def __init__(self, message:str, available_quantity:int, required_quantity:int):
        super().__init__(message)
        self.message = message
        self.available = available_quantity
        self.required = required_quantity


async def out_of_stock_handler(request:Request, exc:OutOfStockError):
    return JSONResponse(
        status_code=400,
        content ={"error":"STOCK_EMPTY" ,"msg":f"{exc.message}", "availableQuantity":exc.available, "requiredQuantity":exc.required}
    )


inventory_handlers = {

OutOfStockError : out_of_stock_handler

}