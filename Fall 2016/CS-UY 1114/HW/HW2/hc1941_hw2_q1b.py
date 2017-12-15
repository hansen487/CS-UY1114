"""
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Program that calculates the BMI of a person using pounds and inches.
"""

pound=float(input("Please enter weight in pounds: "))
inches=float(input("Please enter height in inches: "))
kilo=pound*0.453592
meter=inches*0.0254
bmi=kilo/meter**2   
print("BMI is",bmi)