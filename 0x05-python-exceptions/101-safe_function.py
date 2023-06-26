#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        answer = fct(*args)
        return answer
    except Exception as exep:
        print("Exception: {}".format(exep), file = sys.stderr)
        return None
