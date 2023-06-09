#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    name = dir(hidden_4)
    length = len(name)
    for i in range(0, length):
        if name[i][0:2] != "_":
            print(name[i])     
