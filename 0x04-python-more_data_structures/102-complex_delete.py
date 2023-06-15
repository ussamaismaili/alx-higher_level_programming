#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for i, item in dict(a_dictionary).items():
        if item == value:
            del a_dictionary[i]
    return a_dictionary
