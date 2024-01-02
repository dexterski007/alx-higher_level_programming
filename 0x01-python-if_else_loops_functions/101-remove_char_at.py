#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = ""
    for j, d in enumerate(str):
        if j != n:
            str2 += d
    return (str2)
