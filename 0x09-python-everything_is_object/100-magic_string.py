#!/usr/bin/python3
def magic_string(static={"count": 0}):
    static["count"] += 1
    return str("BestSchool ", * static["count"])[:-2]


for i in range(10):
    print(magic_string())
