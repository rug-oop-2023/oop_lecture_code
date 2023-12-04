def greet_decorator(func):
    def wrapper():
        print("Hello!")
        func()
        print("Goodbye!")
    return wrapper

@greet_decorator
def greet():
    print("Nice to meet you!")

greet() # When called, greet is wrapped by greet_decorator