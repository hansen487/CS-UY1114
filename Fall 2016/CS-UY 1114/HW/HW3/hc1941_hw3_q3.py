 """
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Program that culates the cost of a long-distance call
"""

day=str(input("Enter the day the call started at: "))
time=int(input("Enter the time the call started at (hhmm): "))
duration=int(input("Enter the duration of the call (in minutes): "))
if (day=='Mon' or day=='Tue' or day=='Wed' or day=='Thr' or day=='Fri'):
    if (time>=800 and time<=1800):
        cost=duration*0.4
    else:
        cost=duration*0.25
else:
    cost=duration*0.15
print("This call will cost $",cost)