#!/usr/bin/python3
for r in range(97, 123):
    if chr(r) not in ['q', 'e']:
        print("{:c}".format(r), end="")
