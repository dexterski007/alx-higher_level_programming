#!/usr/bin/python3
def fizzbuzz():
    for j in range(1, 100 + 1):
        if j % 15 == 0:
            print("FizzBuzz", end=" ")
        elif j % 5 == 0:
            print("Buzz", end=" ")
        elif j % 3 == 0:
            print("Fizz", end=" ")
        else:
            print("{:d}".format(j), end=" ")
