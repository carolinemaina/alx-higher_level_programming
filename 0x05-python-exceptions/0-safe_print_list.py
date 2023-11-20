#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    try:
        for a in range(x):
            print(my_list[a], end="")
            n += 1
    except IndexError:
        pass
    finally:
        print("")
    return n
