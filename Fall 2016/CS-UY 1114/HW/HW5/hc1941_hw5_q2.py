"""
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Print triangle of numbers aligned to the right
"""

num=int(input("Enter a positive integer n: "))
printed_string="1"
for i in range (0,num):
    print(" "*(num-1-i)+printed_string)
    printed_string+=str(i+2)