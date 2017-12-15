string=input("Enter an odd length string: ")
print("Middle character:",string[len(string)//2])
print("First half:",string[0:(len(string)//2)])
print("Second half:",string[len(string)//2+1::])