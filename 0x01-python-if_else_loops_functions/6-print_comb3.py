#!/usr/bin/python3
for a in range(0, 10):
    for b in range(a, 10):
        if a < b:
            print("{:d}{:d}".format(a, b),
                end="\n" if a == 8 and b == 9 else ", ")
