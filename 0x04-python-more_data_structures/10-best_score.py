#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    bestscore = 0
    bestkey = None
    for key, value in a_dictionary.items():
        if value > bestscore:
            bestscore = value
            bestkey = key
    return bestkey
