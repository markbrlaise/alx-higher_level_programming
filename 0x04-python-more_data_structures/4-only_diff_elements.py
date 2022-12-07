#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    union = set_1 | set_2
    intersect = set_1 & set_2
    return union - intersect
