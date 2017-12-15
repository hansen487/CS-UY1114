# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 14:47:49 2016

@author: hansen487
"""

def prob1a(n):
    for i in range(1,n+1):
        print(" "*(2*(n-i)),end="")
        for j in range (0,(2*i)-1):
            print("*",end=" ")
        print()

def prob1b(n):
    for i in range (1,n+1):
        for j in range (1,n+1):
            if (j<i):
                print("#",end="")
            elif (j==i):
                print("%",end="")
            elif (j>i):
                print("$",end="")
        print()

def prob2(n):
    for i in range(1,n+1):
        print((n-i)*"."+str(i)*i)

def prob3(n, rand):
    if (n<rand):
        print("Wrong guess. My number is bigger than yours.")
    elif (n>rand):
        print("Wrong guess. My number is smaller than yours.")
    elif (n==rand):
        print("Congrats! You guessed my number!")
        return True

def main():
    n1=int(input("Enter a number for 1a: "))
    prob1a(n1)
    n1b=int(input("Enter a number for 1b: "))
    prob1b(n1b)
    n2=int(input("Enter a number for 2: "))
    prob2(n2)
    import random
    randvar=random.randint(1,100)
    print(randvar)
    print("I thought of a number between 1 to 100! Try to guess it.")
    num=int(input("Try to guess what it is: "))
    while (prob3(num,randvar)!=True):
        num=int(input("Try to guess what it is: "))
main()