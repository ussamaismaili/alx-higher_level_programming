#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    true_false = []
    for i in my_list:
        if i % 2 == 0:
            true_false.append(True)
        else:
            true_false.append(False)
    return (true_false)
