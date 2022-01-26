admin_keys = {"Sajal": "Sajal@1234"}

menu = {1: {'Food Name': 'Butter Chicken', 'Food ID': 1, 'Price': 950, 'Discount': 4, 'Stock': 14},
        2: {'Food Name': 'Roti', 'Food ID': 2, 'Price': 10, 'Discount': 0, 'Stock': 123},
        3: {'Food Name': 'Cake', 'Food ID': 3, 'Price': 1070, 'Discount': 7, 'Stock': 5}}


def add_new_item():
    foodname = input("Enter the foood name: ")
    foodid = int(input("Enter the food id: "))
    price = int(input("Enter the price of the food: "))
    discount = int(input("Enter the discount of food: "))
    stock = int(input("Enter te stock value of food: "))
    menu[foodid] = {
        "Food Name": foodname,
        "Food ID": foodid,
        "Price": price,
        "Discount": discount,
        "Stock": stock
    }
    print(f"The {foodname} is successfully added")
    return menu


def edit_from_item():
    food = int(input("Enter the foodid which you want to edit: "))
    a = input("Enter the food name")
    b = int(input("Enter the price of food"))
    c = int(input("Enter the discount of food"))
    d = int(input("Enter the stock of the food"))
    menu[food]["Food Name"] = a
    menu[food]["Price"] = b
    menu[food]["Discount"] = c
    menu[food]["Stock"] = d
    print("*****Edit food item successfully*****")
    return menu

def show_menu():
    print("*****HERE IS THE MENU OF SAJAL'S DHABA*****")
    for i in menu:
        print("Food Name: ",menu[i]["Food Name"])
        print("Price: ",menu[i]["Price"],"INR")
        print("Food ID: ",menu[i]["Food ID"])

def remove_food_item():
    d = int(input("Enter the food id which you want to exit"))
    menu.pop(d)
    print("Remove food item successfully ")
    return menu
