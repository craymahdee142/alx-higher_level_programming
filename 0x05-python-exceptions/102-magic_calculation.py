#!/usr/bin/python3
def safe_function(fct, *args):
    result = 0
    for i in range(1, 3):
        try:
            if i > 0:
                raise Exception("Too far")
            else:
                result += a ** b / i
        except Exception:
            result = b + a
            break
        return (result)
