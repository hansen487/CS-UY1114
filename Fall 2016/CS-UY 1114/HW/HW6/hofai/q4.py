exp=input("Enter a mathematical expression: ")
exp=exp.split()
oprand1=exp[0]
op=exp[1]
operand2=exp[2]
if (op=='+'):
    output=int(oprand1)+int(operand2)
elif (op=='-'):
    output=int(oprand1)-int(operand2)
elif (op=='*'):
    output=int(oprand1)*int(operand2)
elif (op=='/'):
    output=int(oprand1)/int(operand2)
print(" ".join(exp),'=',output)