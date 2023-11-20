#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    tot = 0
    for a in range(x):
        try:
            print("{:d}".format(my_list[a]), end="")
            tot += 1
        except (ValueError, TypeError):
            pass
    print()
    return tot