"""
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Use Turtle, math operands, conditional statements, and math module functions for this lab.
"""

#Warmup Problem
"""
language=input("Please enter a language: ")
if (language=="en"):
    print("Hello, world!")
elif (language=="es"):
    print("¡Hola mundo!")
elif (language=="cn"):
    print("你好，世界!")
elif(language=="fr"):
    print("Bonjour le monde!")

even_odd=int(input("Enter a number: "))
if (even_odd%2==0):
    print("Even")
else:
    print("Odd")
"""   
#Problem 1
"""
input_num=int(input("Please enter an integer less than 100: "))
display_num=input_num
if (input_num>=50):
    roman_num="L"
    input_num=input_num-50
if (input_num>=10):
    roman_num=roman_num+"X"
    input_num=input_num-10
if (input_num>=10):
    roman_num=roman_num+"X"
    input_num=input_num-10
if (input_num>=10):
    roman_num=roman_num+"X"
    input_num=input_num-10
if (input_num>=10):
    roman_num=roman_num+"X"
    input_num=input_num-10
if (input_num>=5):
    roman_num=roman_num+"V"
    input_num=input_num-5
if (input_num>=1):
    roman_num=roman_num+"I"
    input_num=input_num-1
if (input_num>=1):
    roman_num=roman_num+"I"
    input_num=input_num-1
if (input_num>=1):
    roman_num=roman_num+"I"
    input_num=input_num-1
if (input_num>=1):
    roman_num=roman_num+"I"
    input_num=input_num-1
print(display_num,"in Roman numerals is:",roman_num)
"""
#Problem 2
"""
name=input("Please enter your name: ")
grad_year=int(input("Please enter your graduation year: "))
cur_year=int(input("Please enter a current year: "))
if (grad_year-cur_year>4):
    print(name,"is not in college yet.")
elif (grad_year-cur_year==4):
    print(name,"is a freshman.")
elif (grad_year-cur_year==3):
    print(name,"is a sophomore.")
elif (grad_year-cur_year==2):
    print(name,"is a junior.")
elif (grad_year-cur_year==1):
    print(name,"is a senior.")
else:
    print(name,"already graduated.")
"""
#Problem 3
"""
time=int(input("Please enter a time in 24 hr format: "))
if (time<=1200):
    print(time,"in 12 hr format is:",time)
else:
    new_time=time-1200
    print(time,"in 12 hr format is:",new_time)
"""
#Problem 4
"""
a_tri=int(input("Please enter the first leg: "))
b_tri=int(input("Please enter the second leg: "))
c=int(input("Pleae enter the hypotenuse: "))
if (a_tri**2+b_tri**2==c**2):
    print(a_tri,b_tri,"and",c,"form a right triangle.")
else:
    print(a_tri,b_tri,"and",c,"do not form a right triangle.")
"""
#Problem 5
"""
a=float(input("Please enter a: "))
b=float(input("Please enter b: "))
if (a==0 and b==0):
    print("There are infinitely many solutions.")
if (a==0):
    print("There is no solution.")
else:
    x=-b/a
    print("The equation has single solution and x =",x)
"""    

