# try:
#     # code that may cause an exception
# except SomeException:
#     # code to handle the exception


try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")


# raise ValueError("Invalid value")

x = -10
if x < 0:
    raise ValueError("Negative value not allowed: {}".format(x))

# try:
#     # risky operation
# except Exception as e:
#     # handle exception
# finally:
#     # cleanup code

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"The result is {result}")
    finally:
        print("Executing the finally block.")

# Example usage
divide(10, 2)  # This will not raise an exception
divide(10, 0)  # This will raise a ZeroDivisionError

########################################################################

def set_positive_integer(value):
    if not isinstance(value, int) or value <= 0:
        raise ValueError("Value must be a positive integer", value)
    print(f"Setting value to {value}")

try:
    set_positive_integer(-10)
except ValueError as e:
    print(f"Caught an exception: {e}")
    print(f"Arguments: {e.args}")

