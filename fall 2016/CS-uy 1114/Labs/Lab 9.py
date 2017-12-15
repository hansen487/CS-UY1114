def prob1a(lst, item):
    count=0
    for i in lst:
        if i==item:
            count+=1
    return count
    
def prob1b():
    power=int(input("Enter a power: "))
    lst=[]
    for i in range (1,power+1):
        lst.append(2**i)
    return lst
    
def prob1c(lst):
    index=-1
    maximum=0
    for i in range (0,len(lst)):
        if (lst[i]%2==0):
            if lst[i]>maximum:
                maximum=lst[i]
                index=i
    return index
    
def prob1d(lst, k):
    length=len(lst)
    lst2=[]
    for i in range(0,length):
        lst2.append(lst[(i+(length-k))%length])
    return lst2

def prob2(lst1, lst2):
    lst3=[]
    for i in range (0, len(lst1)):
        for j in range (0, len(lst2)):
            if lst1[i]==lst2[j]:
                lst3.append(lst1[i])
    for k in range(0,len(lst3)):
        for l in range (k+1, len(lst3)):
            if lst3[k]==lst3[l]:
                lst3.remove(lst3[l])
    return lst3
    
def prob3a(lst):
    total=0
    for i in lst:
        total+=i**2
    return total
    
def main():
    lst=[]
    print("Please enter numbers, done to stop: ")
    num=input()
    while (num!='done'):
        lst.append(int(num))
        num=input()
    returned=prob3a(lst)
    print("The sum of the squares is:",returned)

main()

import random

def generateBoard():
    board=['-','-','-'],['-','-','-'],['-','-','-']
    symbols=['X','O','-']
    for i in range(3):
        for j in range(3):
            board[i][j]=symbols[random.randint(0,2)]
    return board

def checkwin(board):
    win=False
    for i in range(3):
        if (board[i][0]==board[i][1] and board[i][1]==board[i][2]):
            win=True
            row=i
            column=0
    for j in range(3):
        if (board[0][j]==board[1][j] and board[1][j]==board[2][j]):
            win=True
            row=0
            column=j
    if (board[0][0]==board[1][1] and board[1][1]==board[2][2]):
        win=True
        row=0
        column=0
    elif (board[0][2]==board[1][1] and board[1][1]==board[2][0]):
        win=True
        row=0
        column=2
    if win==True:
        if (board[row][column]=='-'):
            print("Tie")
        else:
            print(board[row][column],"won")
    else:
        print("Tie")

def main2():
    board=generateBoard()
    for i in range(3):
        for j in range(3):
            print(board[i][j],end=" ")
        print()
    checkwin(board)

main2()
    
        