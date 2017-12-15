"""
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Prints a month based on user inputted start date.
"""
def print_month_calendar(num_of_days, starting_day):
    print("Mon"+"\t"+"Tue"+"\t"+"Wed"+"\t"+"Thr"+"\t"+"Fri"+"\t"+"Sat"+"\t"+"Sun")
    date=1
    for i in range (1, num_of_days+starting_day):
        if (i<starting_day):
            print("", end="\t")
        else:
            print(str(date),end="\t")
            date+=1
            if i%7==0:
                if (date!=num_of_days+1):
                    print()
    print()
    print()
    if i%7==0:
        i=7
        return i
    else:
        return i%7
        
 