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