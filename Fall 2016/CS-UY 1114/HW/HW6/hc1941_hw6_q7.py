# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 15:10:48 2016

@author: hansen487
"""

def firstword(sentence):
    words=sentence.split()
    return words[0]

def removefirst(sentence):
    words=sentence.split()
    removed=""
    for i in range(1, len(words)-1):
        removed+=words[i]+" "
    removed+=words[i+1]
    return removed

def reverse(sentence):
    reversed_array=removefirst(sentence).split()
    reversed_array=reversed_array[::-1]
    reversed_string=""
    for i in range(0, len(reversed_array)):
        reversed_string+=reversed_array[i]+" "
    reversed_string+=firstword(sentence)
    return reversed_string

def main():
    string=input("Please enter a string to be reversed: ")
    print(reverse(string))

main()