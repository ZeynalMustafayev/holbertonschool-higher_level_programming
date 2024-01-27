#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(sys.argv[1])
        op = sys.argv[2]
        b = int(sys.argv[3])
        if op == "+":
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif op == "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif op == "*":
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif op == "/":
            if b != 0:
                print("{:d} / {:d} = {}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
