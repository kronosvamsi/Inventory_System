""" Import the all exceptions classes and handlers """

from .inventory_errors import inventory_handlers, OutOfStockError, InventoryNotFoundError
from .products_errors import ProductNotFoundError, NegativeQuantityError, NewQuantityError, product_handlers
from .db_exception import db_exc_handler

all_exceptions_handlers = {
    **inventory_handlers,       ### dict joining
    **product_handlers
}