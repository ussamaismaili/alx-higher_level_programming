#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    _sum = 0
    size = 0
    for _tuple in my_list:
        _sum += _tuple[0] * _tuple[1]
        size += _tuple[1]
    return _sum / size
