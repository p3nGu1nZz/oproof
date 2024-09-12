from functools import wraps
from .args import Args
from .log import Log
from .error import handle_error

def args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        parsed_args = Args().parse()
        return func(parsed_args, *args, **kwargs)
    return wrapper

def log_and_handle_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            Log.start_main_function()
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            handle_error(e, debug=True)
            Log.error(f"Error in {func.__name__}: {e}")
            raise
    return wrapper
