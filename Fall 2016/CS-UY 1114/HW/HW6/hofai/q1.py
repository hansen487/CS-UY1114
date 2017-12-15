import random
rand=random.randint(1,100)
print("I thought of a number between 1 and 100! Try to guess it.")
maximum=100
minimum=1
userinput=0
tries=5
counter=0
print(rand)
while (counter!=6):
     print("Range: [",minimum,", ",maximum,"], Number of guesses left: ",tries,sep="")
     userinput=int(input("Your guess: "))
     if(rand==userinput):
        counter+=1
        print("Congrats! You guessed my number in",counter,"guesses.")
     elif (userinput>rand):
        print("Wrong! My number is smaller.")
        if (rand<maximum):
            counter+=1
            maximum=userinput
            tries-=1
     elif (rand>minimum):        
        print("Wrong! My number is bigger.")
        if (userinput>minimum):
            minimum=userinput
        counter+=1
        tries-=1
     if (counter==5):
        print("Out of guesses! My number is",rand)
        counter+=1