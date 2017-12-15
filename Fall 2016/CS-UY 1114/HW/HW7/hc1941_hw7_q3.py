# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 00:11:08 2016

@author: hansen487
"""

string=input("Please enter a string of lowercase letters: ")
previous='`' 
decrease=False
for letter in string:
    if (ord(letter)>ord(previous)):
        increase=True
    else:
        decrease=True
    previous=letter
if decrease!=True:
    print(string,"is increasing.")
else:
    print(string,"is not increasing.")