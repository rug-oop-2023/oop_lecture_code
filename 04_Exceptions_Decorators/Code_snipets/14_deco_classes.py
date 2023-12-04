class MyDecorator:
    def __init__(self, func):
        self.func = func
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        print(f"Call {self.call_count} of {self.func.__name__}")
        return self.func(*args, **kwargs)

@MyDecorator
def greet(name):
    print(f"Hello {name}!")


greet("Alice")
greet("Alice")
