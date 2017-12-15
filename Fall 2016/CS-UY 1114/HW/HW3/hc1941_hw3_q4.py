"""
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Program that factors a quadratic equation
"""
a=float(input("Please enter the value of a: "))
b=float(input("Please enter the value of b: "))
c=float(input("Please enter the value of c: "))
if (a==0 and b==0 and c==0):
    print("There are an infinite number of solutions.")
elif (a==0 and b==0):
    print("There are no solutions.")
else:
    if (b**2-4*a*c<0):
        print("There are no real solutions.")
    elif ((-b/2*a)**2==c):
        solution=-(c**1/2)
        print("This equation has single real solution x=",solution)
    else:
        solution1=(-b+(b**2-4*a*c)**0.5)/(2*a)
        solution2=(-b-(b**2-4*a*c)**0.5)/(2*a)
        print("This equation has two real solutions x=",solution1,"and",solution2)