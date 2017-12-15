# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 16:06:12 2016

@author: hansen487
"""
'''#1
string=input("Please enter a string: ")
for letter in string:
    if (letter.isupper()==True):
        print(letter.lower(),end="")
    elif (letter.islower()==True):
        print(letter.upper(), end="")
    else:
        print(" ",end="")

#2
name1=input("Please enter name 1: ")
name2=input("Please enter name 2: ")
a1=name1.split(", ")
a2=name2.split()
if (a1[0]==a2[1] and a1[1]==a2[0]):
    print("The two names are equal!")
else:
    print("The two names are not equal.")

#3a
s=input("Please enter a string: ")
test=input("Please enter a letter: ")
count=0
for letter in s:
    if (test==letter):
        count+=1
print("Letter",test,"appears",count,"times in the string.")

#3b
s=input("Please enter a string: ")
test=input("Please enter a letter: ")
count=0
counter=0
while (counter<len(s)):
    if (test==s[counter]):
        count+=1
    counter+=1
print("Letter",test,"appears",count,"times in the string.")

#4a
s=input("Input a number: ")
even=0
odd=0
for letter in s:
    digit=int(letter)
    if (digit%2==0):
        even+=1
    else:
        odd+=1
print(s,"has",even,"even numbers and",odd,"odd numbers.")

#4b
s=input("Input a number: ")
s=int(s)
even=0
odd=0
x=s
while (x>0):
    if (x%2==0):
        even+=1
    else:
        odd+=1
    x//=10
print(s,"has",even,"even numbers and",odd,"odd numbers.")
'''

