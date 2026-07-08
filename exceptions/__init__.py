""" Import the all exceptions classes and handlers """

from .inventory_errors import inventory_handlers, OutOfStockError

all_exceptions_handlers = {
    **inventory_handlers
}