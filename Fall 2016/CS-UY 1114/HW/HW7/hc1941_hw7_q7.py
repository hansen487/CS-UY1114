# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 16:03:20 2016

@author: hansen487
"""

def encode(string):
    encoded=[]    
    repeat=0
    prev=string[0]
    for letter in string:
        if letter==prev:
            repeat+=1
        else:
            encoded.append([prev,repeat])
            repeat=1
        prev=letter
    encoded.append([prev,repeat])
    return encoded

def decode(lst):
    decoded=''
    for i in lst:
        decoded+=i[0]*i[1]
    return decoded