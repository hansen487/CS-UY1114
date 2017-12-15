"""
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Prints a pine tree.
"""

def print_shifted_triangle(n, m, symbol):
    for i in range(1,n+1):
        print(" "*(m+n-i)+symbol*(2*i-1))

def print_pine_tree(n, symbol):
    print()
    for i in range(1,n+1):
        print_shifted_triangle(i+1,(n+1-(i+1)), symbol)

def main():
    triangles=int(input("Please enter the number of triangles: "))
    symb=input("Please enter the symbol: ")
    print_pine_tree(triangles, symb)

main()