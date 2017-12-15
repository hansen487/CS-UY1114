def prob1():
    string=input("Please enter a string: ")
    print("Your string has: ")
    one=0
    zero=0
    for digit in string:
        if (digit=="0" and one!=0):
            print(one,"1's")        
            zero+=1
            one=0
        elif (digit=="0"):
            zero+=1
        if (digit=='1' and zero!=0):
            print(zero,"0's")
            one+=1
            zero=0
        elif (digit=="1"):
            zero=0
            one+=1
    if (one==0):
        print(zero,"0's")
    elif (zero==0):
        print(one,"1's")

def encode(string_list):
    ls=[]
    for string in string_list:
        st=""
        for char in string:
            char=ord(char)
            char+=20
            char%=127
            char=chr(char)
            st+=char
        ls.append(st)
    return ls

def decode(string_list):
    ls=[]
    for string in string_list:
        st=""
        for char in string:
            char=ord(char)
            char-=20
            char%=127
            char=chr(char)
            st+=char
        ls.append(st)
    return ls

def prob2a(ch,n):
    string=""
    for i in range (0,n):
        x=(ord(ch)+i)
        if x>122:
            x-=26
        string+=chr(x)
    return string

def prob2b(myint, n):
    ls=[]
    for i in range(myint,myint+n):
        ls.append(i)
    return ls
    
def find(string, substring, start, end):
    length=len(substring)
    match=-1
    for i in range (start, end-length):
        if string[i:i+length]==substring:
            match=1
    return match 

def multi_find(string, substring, start, end):
    length=len(substring)
    match=[]
    for i in range (start, end-length):
        if string[i:i+length]==substring:
            match.append(i)
    return match 
    
def main1():
    prob1()
    
main1()
def main():
    lst = ["CS 1114 is awesome!", "My phone number is:\n555-123-4567", "P@ssw0rd!"]
    encoded = encode(lst)
    decoded = decode(encoded)
    print("The following should be identical:")
    print("lst:\n" + str(lst))
    print("decoded:\n" + str(decoded))

main()

def main2():
    string=input("Enter a DNA base sequence: ")
    sub=input("Enter a subsequence: ")
    start=int(input("Enter a starting position: "))
    end=(input("Enter an end position (end for length of string): "))
    if end=='end':
        end=len(string)
    else:
        end=int(end)
    if (find(string, sub, start, end)==1):
        print("Substring",sub,"is present within",string)
        print(sub,"is present at the following locations:",multi_find(string, sub, start,end))
    else:
        print("Substring",sub,"is not present within",string)

main2()
    