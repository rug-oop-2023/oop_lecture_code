def set_positive_integer(value):
    if not isinstance(value, int) or value <= 0:
        raise ValueError("Value must be a positive integer", value)
    print(f"Setting value to {value}")

try:
    set_positive_integer(-10)
except ValueError as e:
    print(f"Caught an exception: {e}")
    print(f"Arguments: {e.args}")