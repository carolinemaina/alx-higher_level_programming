#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n = list(my_list)
    for a in range(len(n)):
        if n[a] == search:
            n[a] = replace
    return n
