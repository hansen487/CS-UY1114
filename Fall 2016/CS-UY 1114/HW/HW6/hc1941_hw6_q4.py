"""
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Read and evaluate a mathematical expression.
"""

expression=input("Enter a mathematical expression: ")
array=expression.split()
operand1=int(array[0])
op=array[1]
operand2=int(array[2])
output=0
if (op=='+'):
    output=operand1+operand2
elif (op=='-'):
    output=operand1-operand2
elif (op=='*'):
    output=operand1*operand2
elif (op=='/'):
    output=operand1/operand2
print(expression,"=",output)