#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    count = 0
    if not my_list:
        return ()
    for i in new_list:
        if search == i:
            new_list[count] = replace
        count = count + 1
    return (new_list)
