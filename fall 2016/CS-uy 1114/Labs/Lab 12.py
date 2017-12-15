class BankAccount():
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def withdraw(self, x):
        self.balance -= x
        return self.balance
        
    def deposit(self, x):
        self.balance += x
        return self.balance
    
    def get_balance(self):
        return self.balance

class Bookstore():
    def __init__(self, name, publisher, price, author, ISBN):
        self.name = name
        self.publisher = publisher
        self.price = price
        self.author = author
        self.ISBN = ISBN
    
    def get_name(self):
        return self.name
    
    def get_publisher(self):
        return self.publisher
        
    def get_price(self):
        return self.publisher
    
    def get_author(self):
        return self.author
    
    def get_ISBN(self):
        return self.ISBN
        
class City():
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def get_city_name(self):
        return self.name
    
    def get_city_coordinates(self):
        return "({}, {})".format(self.latitude, self.longitude)
    
    def get_city_latitude(self):
        return self.latitude
        
    def get_city_longitude(self):
        return self.longitude
    
import math
def distance(city1, city2):
    d = math.sqrt((city1.latitude - city2.latitude) ** 2 + (city1.longitude - city2.longitude) ** 2) 
    d = round(d, 4)    
    return d
    
def main():
    my_account = BankAccount("BOA123", 1000)
    print("Current balance is: ", my_account.get_balance()) #prints 1000
    my_account.deposit(100)
    print("Current balance is: ", my_account.get_balance()) #prints 1100
    my_account.withdraw(500)
    print("Current balance is: ", my_account.get_balance()) #prints 600
    my_account.withdraw(1000) #prints an error message
main()

def main2():
    d = []
    city1 = []
    city2 = []
    cities = ["New York", "Boston", "Chicago", "San Francisco", "Miami", "Seattle", "Austin", "Los Angeles", "Las Vegas"]
    latitude = [42.9371, 42.3587, 41.8843, 37.7799, 25.7748, 47.6036, 30.2676, 34.0535, 36.0117]
    longitude = [-75.6107, -71.0567, -87.6325, -122.429, -80.1977, -122.3295, -97.743, -118,2453, -115,1758]    
    for i in range(len(cities) - 1):
        first = City(cities[i], latitude[i], longitude[i])
        for j in range(i+1, len(cities)):
            second = City(cities[j], latitude[j], longitude[j])
            d.append(distance(first, second))
            city1.append(cities[i])
            city2.append(cities[j])
    for i in range(len(d)):
        print("Distance between",city1[i],"and",city2[i],"is",d[i])
main2()

class Shop():
    