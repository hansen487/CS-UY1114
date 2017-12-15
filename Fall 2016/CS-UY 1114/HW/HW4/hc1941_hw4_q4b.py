"""
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Calculate geometric mean of non-empty sequence of positive integers until done is entered.
"""

print("Please  a non-empty sequence of positive integers, each one in a separate line. End your sequence by typing done:")
gm=1
test=0
counter=0
while test!=1:
    user_in=str(input())
    if (user_in=='done'):
        gm=round(gm**(1/counter),4)
        test=1
        print("The geometric mean is:",gm)
    else:
        user_in=int(user_in)
        gm=gm*user_in
        counter+=1
