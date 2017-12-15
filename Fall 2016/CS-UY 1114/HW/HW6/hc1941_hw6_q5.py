"""
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Determines the vowels and consonants in a word.
"""

vowel=0
consonant=0
word=input("Enter a word: ")
for letter in word:
    if (letter=='a' or letter=='A' or letter=='e' or letter=='E' or letter=='i' or letter=='I' or letter=='o' or letter=='O' or letter=='u' or letter=='U'):
        vowel+=1
    else:
        consonant+=1
print(word,"has",vowel,"vowels and",consonant,"consonants.")