#!/usr/bin/env python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        z = i
    else:
        z = i - 32
    print("{}".format(str(z)), end="")
