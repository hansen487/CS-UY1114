"""
CS-UY 1114
Hansen Chen
Katz
hc1941 N11730096
Reverses elements in functions
"""

def reverse_to_new_list(lst):
    lst2 = []
    lst2 = lst[::-1]
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