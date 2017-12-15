vowel=0
consonant=0
word=input("Enter a word: ")
for letter in word:
    if (letter!='a' and letter!='A' and letter!='e' and letter!='E' and letter!='i' and letter!='I' and letter!='o' and letter!='O' and letter!='u' and letter!='U'):
        consonant+=1
    else:
        vowel+=1
print(word,"has",vowel,"vowels and",consonant,"consonants.")