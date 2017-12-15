"""
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Program that converts numbers from one unit to another, and uses math and turtle module that for math and drawing.
"""

#Q2
days_input=int(input("Please enter the number of days: "))
weeks=days_input//7
days=days_input%7
print(days_input,"days is equal to",weeks,"week(s) and",days,"days.")

#Q3
radius=int(input("Please enter the radius: "))
import math
circumference=2*radius*math.pi
area=radius**2*math.pi
print("Circumference of the circle is:",circumference,"and the area of the circle is:",area)

#Q4
import turtle
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.done

#Q6
date_birth=int(input("Please enter your date of birth in yyyymmdd: "))
input_date=int(input("Please input today's date in yyyymmdd: "))
diff=input_date-date_birth
years=(input_date-date_birth)//10000
months=(diff)%1000//100
days=diff%100
print("You are",years,"years,",months,"months,",days,"days old.")

#Q7
ft_one=int(input("Please enter the first length's feet: "))
yd_one=int(input("Please enter the first length's yard: "))
ft_two=int(input("Please enter the second length's feet: "))
yd_two=int(input("Please enter the second length's yard: "))
yards=(yd_one+yd_two+(ft_one+ft_two)//3)
feet=((ft_one+ft_two)%3)
print("Their sum is:",yards,"yards and",feet,"feet.")

