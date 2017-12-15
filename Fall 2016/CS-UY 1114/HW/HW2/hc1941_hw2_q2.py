"""
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Program that calculates total monetary value of coins.
"""

print("Please enter number of coins: ")
quarters=int(input("# of quarters: "))
dimes=int(input("# of dimes: "))
nickels=int(input("# of nickels: "))
pennies=int(input("# of pennies: "))
quarters=quarters*25
dimes=dimes*10
nickels=nickels*5
total=quarters+dimes+nickels+pennies
dollars=total//100
cents=total%100
print("The total is",dollars,"and",cents,"cents")