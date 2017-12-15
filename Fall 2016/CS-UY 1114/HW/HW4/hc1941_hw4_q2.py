"""
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Print an asterisk hourglass of 2n lines
"""
size=int(input("Enter the size of the hourglass: "))
for i in range(0,size):    
    j=1
    k=1
    while k<=i:
        print(" ",end="")
        k+=1
    size_1=size-i
    ast=2*size_1-1
    while j<=ast:
        print("*", end="")
        j+=1
    print()
for i in range(0,size):    
    j=1
    k=i+1
    while k<size:
        print(" ",end="")
        k+=1
    ast=2*(i+1)-1
    while j<=ast:
        print("*",end="")
        j+=1
    print()
    
    