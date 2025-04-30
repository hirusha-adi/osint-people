import traceback
import functools
from datetime import datetime
import inspect
import time
from utils import colored

def handle_errors(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            colored.print_error(f"An error occurred in {func.__name__}: {e}")
            traceback.print_exc() 
            return None 

    return wrapper

def show_function_info(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        signature = str(inspect.signature(func))
        frame = inspect.currentframe().f_back

        colored.print_debug(f"Running: {func_name}")
        colored.print_debug(f"Signature: {signature}")
        colored.print_debug(f"Arguments: Positional: {args}, Keyword: {kwargs}")
        colored.print_debug(f"Time: {datetime.now()}")

        start_time = time.time()
        # ---
        result = func(*args, **kwargs)
        # ---
        end_time = time.time()
        execution_time = end_time - start_time

        colored.print_debug(f"Execution time: {execution_time:.4f} seconds")

        return result
    
    return wrapper
