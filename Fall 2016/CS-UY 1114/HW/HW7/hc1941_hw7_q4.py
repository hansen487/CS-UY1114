# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 15:21:30 2016

@author: hansen487
"""

def max_abs_val(lst):
    maxval=0    
    for i in range (0,len(lst)):
        if (abs(lst[i]))>maxval:
            maxval=abs(lst[i])
    return maxval