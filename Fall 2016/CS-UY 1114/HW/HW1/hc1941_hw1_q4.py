"""
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Program that calculates population.
"""

year=int(input("Please insert the amount of years: "))
sec=31536000
population=307357870+year*(sec//7)-year*(sec//13)+year*(sec//35)
print("The predicted population after",year,"year(s) will be",population)