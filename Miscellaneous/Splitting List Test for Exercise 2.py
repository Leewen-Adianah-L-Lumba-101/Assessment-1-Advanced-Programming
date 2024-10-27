# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 13:02:49 2024

@author: hp
"""

test = ["foo", "bar", " % " "baz", "", "quux"]

test2 = []

for i, val in enumerate(test):
    if "%" in val:
        test2.append(test[i:])
        del test[i:]
        break
    
print(test)
print(test2)
