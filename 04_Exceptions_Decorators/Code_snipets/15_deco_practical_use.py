def logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"The function '{func.__name__}' returned {result}")
        return result
    return wrapper

@logger
def add(x, y):
    return x + y

add(5, 3)  # add returned 8
