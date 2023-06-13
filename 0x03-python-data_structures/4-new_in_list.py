#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_cpy = []
    if (idx < 0):
        return (my_list)
    elif (idx > len(my_list) - 1):
        return (my_list)
    else:
        for i in range(len(my_list)):
            my_list_cpy.append(my_list[i])
        my_list_cpy[idx] = element
        return (my_list_cpy)
