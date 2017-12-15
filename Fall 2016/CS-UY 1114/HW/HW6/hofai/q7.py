def firstword(sentence):
    split=sentence.split()
    return split[0]

def removefirst(sentence):
    split=sentence.split()
    removedfirst=[]
    for i in range(1, len(split)):
        removedfirst.append(split[i])
    return " ".join(removedfirst)

def reverse(sentence):
    first=firstword(sentence)
    reverse=removefirst(sentence).split()
    reversed_string=[]
    for i in range(0, len(reverse)):
        reversed_string.append(reverse[len(reverse)-i-1])
    reversed_string.append(first)
    return " ".join(reversed_string)
def main():
    string=input("Please enter a string to be reversed: ")
    print(reverse(string))

main()