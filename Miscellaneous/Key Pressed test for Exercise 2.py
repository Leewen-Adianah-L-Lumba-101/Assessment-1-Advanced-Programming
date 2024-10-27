# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 21:04:23 2024

@author: hp
"""
from tkinter import *
import tkinter as tk
import random
import msvcrt


jokes = Tk()

keypressed = False

def key_pressed(event):
    global keypressed
    
    keypressed = True
    
    if keypressed == True:
        print("YAY")

jokes.bind("<Key>", key_pressed)
    
jokes.mainloop()

