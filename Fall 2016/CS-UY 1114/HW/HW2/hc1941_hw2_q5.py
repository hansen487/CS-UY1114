"""
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Calculates how long John and Bill have worked.
"""

john_days=int(input("Please enter the number of days John has worked: "))
john_hours=int(input("Please enter the number of hours John has worked: "))
john_minutes=int(input("Please enter the number of minutes John has worked: "))
bill_days=int(input("Please enter the number of days Bill has worked: "))
bill_hours=int(input("Please enter the number of hours Bill has worked: "))
bill_minutes=int(input("Please enter the number of minutes Bill has worked: "))
minutes=(john_minutes+bill_minutes)%60
hours=john_hours+bill_hours+(john_minutes+bill_minutes)//60
hours=hours%24
days=john_days+bill_days+(john_hours+bill_hours)//24
print("The total time both of them worked together is:",days,"days,",hours,"hours, and",minutes,"minutes.")