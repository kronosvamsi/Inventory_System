""" Base DB exception """

from functools import wraps
from exceptions import ProductNotFoundError
import logging

def db_exc_handler(func):
    
    def get_db_session(*args, **kwargs):
        if "db" in kwargs:
            return kwargs['db']
        for arg in args:
            if hasattr(arg, "rollback") and callable(getattr(arg, "rollback")):
                return arg
        return None
    
    def handle_rollback(db_session, error):
        if db_session:
            try:
                logging.warning(f"Rollback Database trnasaction due to error: {str(error)} ")
                db_session.rollback()
            except Exception as rollback_err:
                logging.critical(f"Failed to rollback database: {str(rollback_err)}")

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            db_session = get_db_session(*args, **kwargs)
            handle_rollback(db_session,err)
            raise err
    
    return wrapper
