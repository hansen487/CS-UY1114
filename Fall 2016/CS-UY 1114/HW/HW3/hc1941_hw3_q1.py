"""
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Program that prints and categorizes BMI
"""

weight=float((input("Please enter weight in kilograms: ")))
height=float((input("Please enter height in meters: ")))
bmi=weight/height**2
print("BMI is",bmi)
if (bmi<18.5):
    print("Underweight")
elif (bmi>=18.5 and bmi<=24.9):
    print("Normal")
elif (bmi>=25.0 and bmi<29.9):
    print("Overweight")
else:
    print("Obese")

