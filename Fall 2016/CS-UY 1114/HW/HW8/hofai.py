'''
attach this header at the top of every file
YOUR NAME
CS 1114
NET ID
TEACHER
WHAT THE FUCK DOES THIS PROGRAM DO
'''
#problem1
def reverse_to_new_list(lst):
    lst2 = []
    for i in range(len(lst)):
        lst2.append(lst[len(lst) - 1 - i])
    return lst2
    
def reverse_in_place(lst):
    for i in range(len(lst)):
        lst.append(lst.pop(len(lst) - 1 - i))
    return lst
    
def main():
    lst1 = [1, 2, 3, 4, 5, 6]
    rev_lst1 = reverse_to_new_list(lst1)
    print("After reverse_to_new_list, lst1 is", lst1,"and the returned list is", rev_lst1)
    lst2 = [1, 2, 3, 4, 5, 6]
    print("Before reverse_in_place, lst2 is", lst2)
    reverse_in_place (lst2)
    print("After reverse_in_place, lst2 is", lst2)

main()

#problem2
def create_prefix_lists(lst):
    lst2 = [[]]
    for i in range(0, len(lst)):
        prefix = []
        for j in range (0, i+1):
            prefix.append(lst[j])
        lst2.append(prefix)
    return lst2
    
#problem3a
def clean_data(complete_weather_filename, cleaned_weather_filename)
    '''
    download the hw3 file from the website
    open file 1 for reading
    open file 2 for writing
    in line 1, split the line by commas
    assign the varaibles to city, date, high, low, precipitation (for line in file)
    write these variables onto file 2
    close both files
    '''
#problem3b
'''
do the same thing for problem a, except convert high, low, and precipitation using the provided functions
'''