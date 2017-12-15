"""
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Introductory lab that adds, subracts, and multiplies numbers and converts numbers
"""

print("Hansen Chen")
num1=int(input("Please enter the first integer: "))
num2=int(input("Please enter the second integer: "))
sum=num1+num2
diff=num1-num2
product=num1*num2
print("Their sum is:",sum,". Their product is:",product,". The difference is:",diff)

far_temp=int(input("Please enter a Farenheit temperature: "))
cel_temp=int((far_temp-32)*5/9)
print("In Celsius it is:",cel_temp,". In Farenheit it is:",far_temp,".")

weight_lb=int(input("Please enter a weight in pounds: "))
weight_kg=weight_lb*0.45
weight_oz=weight_lb*16
print("In ounces,",weight_lb,"pounds is",weight_oz,"ounces and",weight_kg,"kilograms.")
