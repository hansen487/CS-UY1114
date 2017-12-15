"""
CS-UY 1114
Hansen Chen
Katz
hc1941 N11730096
Creates a sequence of prefixes from list
"""

def create_prefix_lists(lst):
    lst2 = [[]]
    for i in range(1,len(lst)+1):
        lst3 = []
        for j in range (0,i):
            lst3.append(lst[j])
        lst2.append(lst3)
    return lst2
