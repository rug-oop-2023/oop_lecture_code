def my_decorator(func):
    def wrapper():
        # Do something before the function call
        func()
        # Do something after the function call
    return wrapper


