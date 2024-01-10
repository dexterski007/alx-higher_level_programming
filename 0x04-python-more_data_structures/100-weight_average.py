#!/usr/bin/python3
def weight_average(my_list=[]):

    bigtot = 0
    indice = 0
    for i in my_list:
        a, b = i
        tot = a * b
        bigtot += tot
        indice += b
    numb = bigtot / indice

    return numb
