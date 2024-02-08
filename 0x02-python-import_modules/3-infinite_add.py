#!/usr/bin/python3

if __name__ == "__main__":
    """we are printed"""
    import sys

    to = 0
    for i in range(len(sys.argv) - 1):
        to += int(sys.argv[i + 1])
    print("{}".format(to))
