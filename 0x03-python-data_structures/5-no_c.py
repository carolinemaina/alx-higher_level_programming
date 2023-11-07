#!/usr/bin/python3
def no_c(my_string):
    n = ""
    for e in my_string:
        if e != "c" and e != "C":
            n += e
    return n
