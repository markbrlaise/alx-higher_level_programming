#!/usr/bin/python3
""" Test function find_peak """
find_peak = __import__('6-peak').find_peak

print(find_peak([1, 2, 4, 4, 6, 7, 4]))
print(find_peak([4, 2, 1, 3, 1]))
print(find_peak([]))
print(find_peak([-2, -5, 3, 1]))
