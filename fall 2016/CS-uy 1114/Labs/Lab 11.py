def read_menu(filename):
    f = open(filename, 'r')
    item=[]
    price=[]
    for line in f:
        menu_array=line.split(sep=": ")
        menu_array[1]=menu_array[1].strip('\n')
        if (menu_array[0]!="\n"):
            item.append(menu_array[0])
            price.append(menu_array[1])
    menu={item[x]: price[x] for x in range(len(item))}
    f.close()
    return menu
    
def read_customer_order():
    order=[]
    print("What would you like to order?")
    user=input()
    while (user!='done'):
        order.append(user)
        user=input()
    return order

def compute_price(menu_dictionary, order_list):
    total=0.0
    for i in order_list:
        total+=float(menu_dictionary[i].strip('$'))
    total*=1.085
    total=round(total, 2)
    total='$'+str(total)
    return total

def main():
    filename=input("Please enter a file name: ")
    menu=read_menu(filename)
    orders=read_customer_order()
    total=compute_price(menu, orders)
    print("The total is",total)
main()

def phone_number_checker(phonenumber):
    if (len(phonenumber)==10 and not phonenumber.isalpha()):
        return True
    else: 
        return False

def add_entry(phonebook, name, phonenumber):
    if not phone_number_checker(phonenumber):
        print(phonenumber,"is not valid.")
    elif (name in phonebook):
        print(name,"already exists.")
    else:
        phonebook[name]=int(phonenumber)
    return phonebook
    
def lookup(phonebook, name):
    if ((name in phonebook)==False):
        print("Error, name not present in phonebook.")
    else:
        return phonebook[name]

def print_all(phonebook):
    for key in phonebook:
        print(key,phonebook[key])

def main2():
    f=open("lab11-phonebook.txt")
    phonebook={}
    for line in f:
        lst=line.split()
        lst[0]=lst[0].strip(',')
        name=lst[1]+" "+lst[0]
        number=lst[2]
        add_entry(phonebook, name, number)
    print_all(phonebook)
main2()
    