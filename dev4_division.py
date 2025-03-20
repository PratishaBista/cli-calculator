def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Both inputs must be numbers."
    else:
        return result

# Example usage
print(safe_divide(10, 2))  # Output: 5.0
print(safe_divide(10, 0))  # Output: Error: Division by zero is not allowed.
print(safe_divide(10, "a"))  # Output: Error: Both inputs must be numbers.
