"""
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Convert number to roman numerals
"""

input_num=int(input("Enter decimal number: "))
roman_num=""
display_num=input_num
while (input_num>=1000):
    roman_num+="M"
    input_num-=1000
while (input_num>=500):
    roman_num+="D"
    input_num-=500
while (input_num>=100):
    roman_num+="C"
    input_num-=100
while (input_num>=50):
    roman_num+="L"
    input_num=input_num-50
while (input_num>=10):
    roman_num=roman_num+"X"
    input_num=input_num-10
while (input_num>=5):
    roman_num=roman_num+"V"
    input_num=input_num-5
while (input_num>=1):
    roman_num=roman_num+"I"
    input_num=input_num-1
print(display_num,"in Roman numerals is:",roman_num)