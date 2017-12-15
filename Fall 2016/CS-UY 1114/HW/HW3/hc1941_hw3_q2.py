"""
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Program that computes how much customer pays
"""

item1=int(input("Enter price of first item: "))
item2=int(input("Enter price of second item: "))
clubcard=str(input("Does the customer have a club card? (Y/N): "))
tax=float(input("Enter tax rate, e.g. 5.5 for 5.5% tax: "))
total=item1+item2
print("Base price =",total)
if (item1>item2):
    item2=item2/2
else:
    item1=item1/2
    
total=item1+item2

if (clubcard=='y'):
    total=total*0.9
print("Price after discounts =",total)
tax=tax/100
tax=1+tax
total=total*tax
total=round(total, 2)
print("Total price =",total)