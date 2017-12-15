"""
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Program that calculates if a year is a leap year.
"""
def leap_year_calc(input_year):
    if (input_year%400==0):
        return True
    elif (input_year%4==0 and input_year%100!=0):
        return True
    else:
        return False

