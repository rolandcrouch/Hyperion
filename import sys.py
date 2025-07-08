from tabulate import tabulate

class Shoe:
    def __init__(self,country,code,product,cost,quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost
    
    def get_quantity(self):
        return self.quantity
    
    def __str__(self):
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"

shoe_list = []


def read_shoes_data():
    try:
    #write list to text file including dotted line after each student ID
        with open("/Users/rolandcrouch/Documents/Hyperion Module 1/inventory.txt", "r+") as file:
            next(file)
            for line in file:
                # length of lines
                fields = [f.strip() for f in line.strip().split(",")]
                if len(fields) != 5:
                    raise ValueError ("Invalid line format")
                else:
                    country, code, product, cost, quantity = fields
                    shoe_list.append(Shoe(country, code, product, cost, quantity))

    except FileNotFoundError:
        return "Please ensure file is saved correctly"

def capture_shoes():
    print("Please enter in your SKU below:\n")
    country = input("Which country are you entering the shoe for?:\n")
    code = input("Which code corresponds with this shoe?:\n")
    product = input("What is the shoe's product name?:\n")
    cost = input("What is the total worth of your stock?:\n")
    quantity = input("How much stock do you have?:\n")
    shoe_list.append(Shoe(country,code, product, cost, quantity))

def view_all():
    #for shoe in shoe_list:
    print(tabulate(shoe_list))

read_shoes_data()

capture_shoes()

view_all()


