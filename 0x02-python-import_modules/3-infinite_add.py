#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arguments = sys.argv[1:]
    result = sum(map(int, arguments))
    print(result)
