
from functools import wraps
import time

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} executed in {end-start:.6f} seconds")
        return result
    return wrapper

@timer
def calculate():
    return sum(i*i for i in range(10_000_000))

calculate()
