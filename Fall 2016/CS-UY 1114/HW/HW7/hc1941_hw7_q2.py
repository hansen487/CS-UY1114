# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 23:58:51 2016

@author: hansen487
"""

rshift=int(input("Enter a right shift: "))
s=input("Enter a string with at least one capital letter: ")
for char in s:
    if (char.isupper()==True):
        char=ord(char)+rshift
        while char>90:
            char-=26
        char=chr(char)
    elif (char.islower()==True):
        char=ord(char)+rshift
        while char>123:
            char-=26
        char=chr(char)
    print(char,end="")