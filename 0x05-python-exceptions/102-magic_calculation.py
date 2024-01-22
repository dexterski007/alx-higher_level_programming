#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0
    for i in range(1,3):
        try:
            if i > a:
                raise IndexError("Too far")
            result += a ** b / i
        except IndexError:
            result = a + b
            break
        finally:
            return result
