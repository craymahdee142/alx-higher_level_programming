#!/usr/bin/python3
if __name__ == "__main__":
#prints the result of all addition of arguments
    import sys
    total_value = 0
    for i in range(1, len(sys.argv)):
        total_value += int(sys.argv[i])
    print("{}".format(total_value))
