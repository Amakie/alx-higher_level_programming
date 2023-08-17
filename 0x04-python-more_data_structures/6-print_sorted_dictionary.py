#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    key_set = list(a_dictionary.keys())
    key_set.sort()
    for key in key_set:
        print("{}: {}".format(key, a_dictionary[key]))
