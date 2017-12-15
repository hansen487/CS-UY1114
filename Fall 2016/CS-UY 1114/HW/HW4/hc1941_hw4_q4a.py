"""
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Program that reads sequence of numbers and calculates geometric mean
"""

length=int(input("Please enter the length of the sequence: "))
print("Please enter your sequence:")
gm=1
for i in range (1, length+1):
    user_in=int(input())
    gm=gm*user_in
gm=round(gm**(1/length),4)
print("The geometric mean is:",gm)