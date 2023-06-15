#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    num = 0
    result = 0
    for score, weight in my_list:
        num += score * weight
        result += weight
    weighted_average = num / result
    return (weighted_average)
