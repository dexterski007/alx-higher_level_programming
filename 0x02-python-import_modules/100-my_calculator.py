#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    args = sys.argv[1:]
    totarg = len(args)
    if totarg != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(args[0])
    b = int(args[2])
    if args[1] == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif args[1] == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif args[1] == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif args[1] == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
