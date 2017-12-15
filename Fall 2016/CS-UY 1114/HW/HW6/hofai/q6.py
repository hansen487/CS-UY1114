password=input("Enter a password: ")
upper=0
lower=0
digit=0
special=0
for letter in password:
    if (letter.isdigit()==True):
        digit+=1
    elif (letter.islower()==True):
        lower+=1
    elif (letter.isupper()==True):
        upper+=1
    elif (letter=='!' or letter=='@' or letter=='#' or letter=='$'):
        special+=1
if (upper>=2 and lower>=1 and digit>=2 and special>=1):
    print(password,"is a valid password.")
else:
    print(password,"is not a valid password.")