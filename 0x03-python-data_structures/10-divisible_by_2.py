#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for num in my_list:
        # check if number is divisible by 2
        if num % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return (new_list)
