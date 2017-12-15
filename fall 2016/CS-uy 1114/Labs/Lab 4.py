"""
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Use Turtle, conditional statements, and loops for the lab
"""

#problem1
x=int(input("Please enter a positive integer: "))
n=int(input("Please enter the number of digits: "))
temp=x
sum=0
for i in range(1,n+1):
    sum=sum+temp%10
    temp=temp//10
print("Sum of the last",n,"digits in",x,"is:",sum)

#problem2
p2_x=int(input("Please enter a positive integer: "))
total=0
for i in range(1,p2_x+1):
    total=total+(-1)**(i+1)*(i)
print("Sum is:",total)

#problem3
p3_a=int(input("Please enter a positive integer as the dividend: "))
p3_b=int(input("Please enter a positive integer as the divisor: "))
p3_a2=p3_a
count=0
while (p3_a2-p3_b>=0):
    p3_a2=p3_a2-p3_b
    count+=1
print("Quotient of",p3_a,"divided by",p3_b,"is:",count)

#problem4
p3_a=int(input("Please enter a positive integer as the dividend: "))
p3_b=int(input("Please enter a positive integer as the divisor: "))
p3_a2=p3_a
while (p3_a2-p3_b>=0):
    p3_a2=p3_a2-p3_b
print("Quotient of",p3_a,"divided by",p3_b,"is:",p3_a2)

#problem5a
n_cube=int(input("Enter a number n: "))
print("The first",n_cube,"cubes are: ")
for i in range(1,n_cube+1):
    print(i**3)

#problem5b
n_cubep=int(input("Enter a number n: "))
print("The perfect cubes that are less than",n_cubep,"are: ")
j=1
while j**3<n_cubep:
    print(j**3)
    j+=1

#problem5c
n_cubes=int(input("Enter a number n: "))
print("The sum of the cubes are: ")
sum_cubes=0
for i in range(1,n_cubes+1):
    sum_cubes+=i**3
print(sum_cubes)

#problem6
n_matrix=int(input("Please enter the dimension of the matrix: "))
for i in range(1,n_matrix+1):
    for j in range(1, n_matrix+1):
        if i==j:
            print("o",end="")
        else:
            print("x",end="")
    print()

#problem7
less_100=int(input("Enter a number less than 100: "))
for i in range(1,less_100+1):
    if (i%3==0 and i%5==0):
        print("FizzBuzz",end=" ")
    elif (i%3==0):
        print("Fizz", end=" ")
    elif (i%5==0):
        print("Buzz",end=" ")
    else:
        print(i, end=" ")

#problem8
import turtle
sides=int(input("Enter the number of sides: "))
turn=((sides-2)*180)/sides
for i in range(1,sides+1):
    turtle.forward(100)
    turtle.left(180-turn)
turtle.done()