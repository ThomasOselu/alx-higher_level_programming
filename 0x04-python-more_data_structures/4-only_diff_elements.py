#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_1.symmetric_difference_update(set_2)
    return (set_1)