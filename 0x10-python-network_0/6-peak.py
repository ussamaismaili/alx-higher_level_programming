#!/usr/bin/python3
""" module doc """


def find_peak(list_of_integers):
    """ function doc """
    if list_of_integers:
        n = len(list_of_integers)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if list_of_integers[mid] > list_of_integers[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return list_of_integers[left]
