"""
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Converts Roman numerals to numbers
"""

romnum=str(input("Enter number in the simplified Roman system: "))
num=0
for letter in romnum:
    if (letter=='M'):
        num+=1000
    elif (letter=='D'):
        num+=500
    elif (letter=='C'):
        num+=100
    elif (letter=='L'):
        num+=50
    elif (letter=='X'):
        num+=10
    elif (letter=='V'):
        num+=5
    elif (letter=='I'):
        num+=1
print(romnum,"is",num)