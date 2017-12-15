"""
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Number guessing game
"""

import random

print("I thought of a number between 1 and 100! Try to guess it.")
num=random.randint(1,100)

user=0
minimum=1
maximum=100
tries=0
guesses_left=5
while(user!=num):
    print("Range: [",minimum,", ",maximum,"], Number of guesses left: ",guesses_left,sep="")
    user=int(input("Your guess: "))
    if (guesses_left==1):
        print("Out of guesses! My number is",num)
        user=num
    elif (user<num):
        print("Wrong! My number is bigger.")
        if (user>minimum):
            minimum=user
        guesses_left-=1
        tries+=1
    elif (user>num):
        print("Wrong! My number is smaller.")
        if (user<maximum):
            maximum=user
            guesses_left-=1
            tries+=1
    elif(user==num):
        tries+=1
        print("Congrats! You guessed my number in",tries,"guesses.")