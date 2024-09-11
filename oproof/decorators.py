from functools import wraps
from .args import Args

def args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        parsed_args = Args().parse()
        return func(parsed_args, *args, **kwargs)
    return wrapper
