"""
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Print a power table using for loops.
"""

for i in range (1, 6):
    for j in range (1, 11):
        output=j**i
        print (output, end="\t")
    print()
