# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 15:26:29 2016

@author: hansen487
"""

def find_all(lst, val):
    occur=[]
    for i in range (0,len(lst)):
        if lst[i]==val:
            occur.append(i)
    return occur