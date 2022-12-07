#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    for i in my_list:
        if search == replace:
            new_list.append(replace)
        else:
            new_list.append(i)
