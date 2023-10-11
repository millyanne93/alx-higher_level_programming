#!/usr/bin/python3
def weight_average(my_list=[]):
    num = 0
    denom = 0
    if my_list:
        for i in range(len(my_list)):
            num += my_list[i][0] * my_list[i][1]
            denom += my_list[i][1]
        average = num / denom
        return average
    else:
        return 0
