#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = 0
    length = len(sys.argv)
    for i in range(1, length):
        add += int(sys.argv[i])
    print("{}".format(add))
