"""
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Prints middle character and each half of the string
"""

oddstring=input("Enter an odd length string: ")
mid=len(oddstring)//2
print("Middle character:",oddstring[mid])
print("First half:",oddstring[0:mid])
print("Second half:",oddstring[mid+1::])