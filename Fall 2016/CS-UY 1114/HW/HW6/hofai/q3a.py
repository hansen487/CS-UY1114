character=input("Enter a character: ")
if (character.isnumeric()==True):
    print(character,"is a digit.")
elif (character.islower()==True):
    print(character,"is a lower case letter.")
elif (character.isupper()==True):
    print(character,"is an upper case letter.")
else:
    print(character,"is a non-alphanumeric character.")


character=input("Enter a character: ")
if (character>='0' and character<='9'):
    print(character,"is a digit.")
elif (character>='A' and character<='Z'):
    print(character,"is an upper case letter.")
elif (character>='a' and character<='z'):
    print(character,"is a lower case letter.")
else:
    print(character,"is a non-alphanumeric character.")