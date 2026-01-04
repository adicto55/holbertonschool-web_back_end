#!/usr/bin/python3
def safe_print_division(a, b):
    """Divide 2 integers and print the result in finally block"""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
    return result
