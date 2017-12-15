"""
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Determines if a character is upper, lower, digit, or non-alphanumeric.
"""

char=input("Enter a character: ")
if (char.isupper()==True):
    print(char,"is an upper case letter.")
elif (char.islower()==True):
    print(char,"is a lower case letter.")
elif (char.isnumeric()==True):
    print(char,"is a digit.")
else:
    print(char,"is a non-alphanumeric character.")
    
    
char=input("Enter a character: ")
if (char>='A' and char<='Z'):
    print(char,"is an upper case letter.")
elif (char>='a' and char<='z'):
    print(char,"is a lower case letter.")
elif (char>='0' and char<='Y'):
    print(char,"is a digit.")
else:
    print(char,"is a non-alphanumeric character.")