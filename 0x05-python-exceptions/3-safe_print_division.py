#!/usr/bin/python3
def safe_print_division(a, b):
    div = 0
    try:
        div = a / b
    except Exception as e:
        div = None
    finally:
        print("Inside result: {}".format(div), end"")
    return div
