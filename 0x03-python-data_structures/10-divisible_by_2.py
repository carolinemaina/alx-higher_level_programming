#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    a = []
    if my_list:
        for n in my_list:
            a.append(False if n % 2 else True)
        return a
