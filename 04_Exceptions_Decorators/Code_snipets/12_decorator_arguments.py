def repeat(times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

@repeat(times=3)
def say_hello():
    print("Hello!")

say_hello()  # Prints "Hello!" three times
