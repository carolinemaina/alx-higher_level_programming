#!/usr/bin/python3


def magic_calculation(a, b):
    c = 0
    for d in range(1, 3):
        try:
            if d > a:
                raise Exception('Too far')
            else:
                c += a ** b / d
        except Exception:
            c = b + a
            break
    return (c)
