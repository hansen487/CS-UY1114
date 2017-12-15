# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 15:32:57 2016

@author: hansen487
"""

def add_list(lst1, lst2):
    total=[]
    for i in range (0,len(lst1)):
        total.append(int(lst1[i])+int(lst2[i]))
    return total  

def append_list(lst):
    number=input()
    while (number!='done'):
        lst.append(number)
        number=input()
    print()

def check_length(lst1, lst2):
    if (len(lst1)==len(lst2)):
        print("The sums are: ")        
        listsum=add_list(lst1, lst2)
        return listsum
    elif (len(lst1)>len(lst2)):
        print("Lists are different lengths.")
        return False

def main():
    print("Please print the numbers for list 1: ")
    list1=[]
    list2=[]
    append_list(list1)
    print("Please print the numbers for list 2: ")
    append_list(list2)
    total=check_length(list1, list2)
    if total!=False:
        for num in total:
            print(num)

main()