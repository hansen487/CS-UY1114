"""
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Program that prints numbers smaller than n with more even than odd digits.
"""

n=int(input("Enter a positive integer: "))
for i in range (1,n+1):
    string=str(i)
    even=0
    odd=0
    for digit in string:
        num=int(digit)
        if (num%2)==0:
            even+=1
        else:
            odd+=1
    if (even>odd):
        print(i)