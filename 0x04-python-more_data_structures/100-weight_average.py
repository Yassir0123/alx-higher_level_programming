#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    um = 0
    en = 0

    for tup in my_list:
        um += tup[0] * tup[1]
        en += tup[1]

    return (um / en)
