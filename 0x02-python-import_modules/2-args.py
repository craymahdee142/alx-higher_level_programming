#!/usr/bin/python3
if __name__ == "__main__":
    import sys
#prints the number and list of argument
    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif ocunt == 1:
        print("1 argument:"")
    else:
        print("{} arguments:".format(count))
    for in range(count):
        print("{}: {}".format(i + 1, sys.argc[i + 1]))
