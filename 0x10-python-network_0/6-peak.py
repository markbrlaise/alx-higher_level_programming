#!/usr/bin/python3
def find_peak(list_of_integers):
    """function that finds the peak of unsorted integers"""
    if list_of_integers == None or list_of_integers == []:
        return None
    length = len(list_of_integers)
    if length == 1:
        return list_of_integers[0]
    i = 0
    #trend = list_of_integers[0] - list_of_integers[1]
    while (i < (length - 2)):
        before = list_of_integers[i] - list_of_integers[i + 1]
        after = list_of_integers[i + 1] - list_of_integers[i + 2]
        #print('hola')
        if (before * after) < 0 and\
                (list_of_integers[i + 1] > list_of_integers[i + 2]):
            return list_of_integers[i + 1]
        i += 1
    return max(list_of_integers)
