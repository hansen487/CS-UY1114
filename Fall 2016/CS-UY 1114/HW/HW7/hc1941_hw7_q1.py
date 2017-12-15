# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 23:57:05 2016

@author: hansen487
"""

string=input("Please enter a line of text: ")
char=input("please enter the character you want to remove: ")
for letter in string:
    if (letter!=char):
        print(letter,end="")