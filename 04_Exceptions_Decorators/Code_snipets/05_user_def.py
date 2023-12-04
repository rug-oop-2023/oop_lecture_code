# class MyCustomError(Exception):
#     pass


class TooSmallValueError(Exception):
    """Exception raised when the input value is too small."""
    def __init__(self, value, message="Value is too small"):
        self.value = value
        self.message = message
        super().__init__(self.message, self.value)

    def __str__(self):
        return f'{self.message} --> {self.value}'

def check_value(value):
    if value < 10:
        raise TooSmallValueError(value)

# Using the custom exception
try:
    check_value(14)
except TooSmallValueError as e:
    print(e)  # Output: Value is too small --> 5

