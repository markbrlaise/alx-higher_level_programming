#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary
    for k, v in new_dict:
        v = v * 2
    return new_dict
