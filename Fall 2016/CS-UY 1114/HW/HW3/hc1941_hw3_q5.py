"""
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Program that classifies triangles based off user inputted lenghts
"""

print("Please enter lenghts of a triangle's sides")
a=float(input("Length of first side: "))
b=float(input("Length of second side: "))
c=float(input("Length of third side: "))
if (a==b and b==c):
    print(a,", ",b,", ",c," form an equilateral triangle.",sep="" )
elif (a==b or b==c or a==c):
    a_sqr=round(a**2, 5)
    b_sqr=round(b**2, 5)
    c_sqr=round(c**2, 5)
    if (a_sqr+b_sqr==c_sqr):
        print(a,", ",b,", ",c," form a right isosceles triangle.",sep="" )
    else:
        print(a,", ",b,", ",c," form an isosceles triangle.",sep="" )
else:
    print(a,", ",b,", ",c," form neither an equilateral nor isosceles triangle.",sep="" )