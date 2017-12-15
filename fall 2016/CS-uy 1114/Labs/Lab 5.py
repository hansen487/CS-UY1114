"""
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Use loops for Lab 5
"""

#Problem4
factorial=int(input("Please enter a positive integer: "))
i=1
n=1
for i in range(1,factorial):
    n=n*(i+1)
    i+=1
print(n)

#Problem5
dog_year=int(input("Input a dog's age in human years: "))
i=0
if dog_year <=2:
    dog_age=dog_year*10.5
else:
    dog_year=dog_year-2
    dog_age=0
    for i in range (1, dog_year+1):
        dog_age+=4
    dog_age+=21
print("The dog's age in human years is",dog_age)

#Problem6
a=int(input("Enter length of first string: "))
b=int(input("Enter length of second string: "))
c=0
a_new=a
while a>0:
   if a%10!=b%10:
       c=c+1
   a//=10
   b//=10
print(c)
