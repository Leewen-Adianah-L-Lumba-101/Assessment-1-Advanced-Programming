# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 15:41:45 2024

@author: hp
"""

import random

score = 0
lives = 3

no1 = (random.randint(1,99))
no2 = (random.randint(1,99))

if no1 > no2: 
    print(f"{no1} - {no2} = ")
    
    answer = int(input("Your answer: "))
    
    if answer == no1-no2:
        print("You did it!")
    else:
        print("Wrong!")
    
else: 
    print(f"{no1} - {no2} = ")


