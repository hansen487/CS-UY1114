def circular_shift_list1(lst, k):
    length=len(lst)
    for i in range(length-k):
        lst.append(lst[i])
    for i in range(length-k):
        lst.pop(0)
    return lst
    
def remove_below_avg(lst):
    total=0
    for i in lst:
        total+=i
    avg=total/len(lst)
    i=0
    while i<len(lst):
        if lst[i]<=avg:
            lst.remove(lst[i])
        else:
            i+=1
    return lst
    
def writeName(filename, firstName, lastName):
    f=open(filename,'w')
    name=firstName+" "+lastName
    f.write(name)
    f.close()
    
def writeRandNumbers(filename, n):
    import random
    f=open(filename, 'w')
    for i in range(n):
        f.write(str(random.randint(1,100))+"\n")
    f.close()
    
def sumColumn(filename):
    f=open(filename, 'r')
    total=0
    for line in f:
        total+=int(line)
    return total

