from functools import wraps

def cache(max_size=None):
    cache_store = {}
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Check if the function has been called with the same arguments before
            key = (args, frozenset(kwargs.items()))
            if key in cache_store:
                return cache_store[key]
            else:
                # If not, call the function and store the result in the cache
                result = func(*args, **kwargs)
                cache_store[key] = result
                
                # If max_size is provided and cache size exceeds max_size, remove the oldest entry
                if max_size is not None and len(cache_store) > max_size:
                    oldest_key = next(iter(cache_store))
                    del cache_store[oldest_key]
                    
                return result
        return wrapper
    return decorator

# Example usage:
@cache(max_size=3)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Output: 55 (Calculates Fibonacci(10) and stores in cache)
print(fibonacci(5))   # Output: 5  (Retrieves Fibonacci(5) from cache)
print(fibonacci(7))   # Output: 13 (Calculates Fibonacci(7) and stores in cache)
print(fibonacci(6))   # Output: 8  (Retrieves Fibonacci(6) from cache)
