#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_v = max(a_dictionary.values())
        for i in a_dictionary:
            if a_dictionary[i] == max_v:
                return a_dictionary[i]
    else:
        return ()
