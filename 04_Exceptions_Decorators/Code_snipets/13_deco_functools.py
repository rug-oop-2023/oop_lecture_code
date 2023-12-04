from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Something before {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Something after {func.__name__}")
        return result
    return wrapper

@my_decorator
def greet(name):
    """Greets a person."""
    print(f"Hello {name}!")

print(greet.__name__)  # Without wraps, this would be 'wrapper' instead of 'greet'
print(greet.__doc__)   # Greets a person.
