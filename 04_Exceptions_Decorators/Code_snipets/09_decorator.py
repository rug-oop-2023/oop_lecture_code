# def my_decorator(func):
#     def wrapper():
#         # Do something before
#         func()
#         # Do something after
#     return wrapper


def greet_decorator(func):
    def wrapper():
        print("Hello!")
        func()
        print("Goodbye!")
    return wrapper

@greet_decorator
def greet():
    print("Nice to meet you!")

greet()