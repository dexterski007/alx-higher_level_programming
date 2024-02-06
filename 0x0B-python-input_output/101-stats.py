#!/usr/bin/python3
""" this is a module for seekndestroy files """


from sys import stdin

statuses = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0,
}

size = 0
increm = 0


def printe():
    """  print log summary """
    print("File size: {}".format(size))
    for key, value in sorted(statuses.items()):
        if value > 0:
            print("{:s}: {:d}".format(key, value))


try:
    for line in stdin:
        subline = line.split()
        if len(subline) >= 2:
            stat = subline[-2]
            size += int(subline[-1])
            if stat in statuses:
                statuses[stat] += 1
        increm += 1

        if increm % 10 == 0:
            printe()
    printe()
except KeyboardInterrupt as ex:
    printe()
