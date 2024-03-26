# Documentation for `@cache()` & `@wraps()`

1. **@wraps**:

   * `@wraps`is a decorator in Python used to preserve the metadata of the original function when decorating it with another function.

   * It copies attributes such as`__name__`,`__doc__`, and`__module__`from the original function to the wrapper function, ensuring that the decorated function behaves as much like the original function as possible.

   * It is often used when creating decorators to maintain the identity of the decorated function for debugging and introspection purposes.

Example:

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before calling the function
        result = func(*args, **kwargs)
        # Do something after calling the function
        return result
    return wrapper

```

1. **@cache**:

   * `@cache`is a custom decorator that can be used to cache the results of function calls and retrieve them from the cache if the same arguments are provided again.

   * It is often used to optimize functions that are computationally expensive or have repeated calls with the same arguments.

   * In the example provided earlier,`@cache`is a decorator function that takes a function as input and returns a wrapped function that performs caching.

Example:

```python
def cache(func):
    cache_store = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in cache_store:
            return cache_store[key]
        else:
            result = func(*args, **kwargs)
            cache_store[key] = result
            return result

    return wrapper

```

In the`@cache`example, the`wrapper`function is responsible for caching the results of the original function (`func`) and returning them if the same arguments are provided again. The`@wraps`decorator ensures that the wrapper function retains the metadata of the original function.
