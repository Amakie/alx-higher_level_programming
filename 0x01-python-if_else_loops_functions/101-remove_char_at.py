#!/usr/bin/python3

def remove_char_at(str, n):
    n_str = ""
    pos = -1

    for letter in str:
        pos = pos + 1
        if (pos == n):
            continue
        n_str = n_str + letter
    return n_str
