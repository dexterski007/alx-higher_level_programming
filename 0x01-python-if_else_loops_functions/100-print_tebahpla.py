#!/usr/bin/python3
for j in range(25, -1, -1):
    d = j + ord('A')
    if j % 2 == 1:
        d += 32
    print("{:c}".format(d), end="")
