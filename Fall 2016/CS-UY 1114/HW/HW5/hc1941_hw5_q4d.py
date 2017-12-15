"""
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Prints a calendar for a user-inputted year.
"""
def print_year_calendar(year, start_day):
    print("January",year)
    end_date=print_month_calendar(31, start_day)%7+1
    print("February",year)
    if (leap_year_calc(year)==True):
        end_date=print_month_calendar(29,end_date)%7+1
    else:
        end_date=print_month_calendar(28,end_date)%7+1
    print("March",year)
    end_date=print_month_calendar(31,end_date)%7+1
    print("April", year)
    end_date=print_month_calendar(30,end_date)%7+1
    print("May", year)
    end_date=print_month_calendar(31,end_date)%7+1
    print("June",year)
    end_date=print_month_calendar(30,end_date)%7+1
    print("July",year)
    end_date=print_month_calendar(31,end_date)%7+1
    print("August",year)
    end_date=print_month_calendar(31,end_date)%7+1
    print("September", year)
    end_date=print_month_calendar(30,end_date)%7+1
    print("October",year)
    end_date=print_month_calendar(31,end_date)%7+1
    print("November",year)
    end_date=print_month_calendar(30,end_date)%7+1
    print("December",year)
    print_month_calendar(31,end_date)%7+1
       
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

def leap_year_calc(input_year):
    if (input_year%400==0):
        return True
    elif (input_year%4==0 and input_year%100!=0):
        return True
    else:
        return False
        
def main():
    input_year=int(input("Please enter a year: "))
    day_start=int(input("Please enter a starting date: "))
    print_year_calendar(input_year,day_start)
    
main()