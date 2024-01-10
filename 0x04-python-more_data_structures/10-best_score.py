#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best_keys = max(a_dictionary, key=a_dictionary.get)
        return best_keys

    else:
        return None
