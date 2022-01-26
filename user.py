import admin as ad

class User:
    login_info = {}

    def __init__(self, name, phoneno, email, address, password):
        self.name = name
        self.number = phoneno
        self.email = email
        self.address = address
        self.password = password
        User.login_info[self.name] = self.password
        self.profile = {}
        self.order_history = {}

    @classmethod
    def login(cls, username, password):
        if cls.login_info.get(username) == password:
            print("You're are successfully logged in.....")
            return True
        else:
            print("SORRY! These are the Wrong Credentials")
            return False

    def see_profile(self):
        self.profile[self.name] = {
            "Full Name": self.name,
            "Phone Number": self.number,
            "E-Mail": self.email,
            "Address": self.address,
            "Password": self.password
        }
        return self.profile

    def update_profile(self):
        x = input("What you want to update in your profile..")
        y = input("And changes to the new one: ")
        self.profile[x] = y
        print("Your Profile is Successfully Updated")
        return self.profile

    def place_order(self):
        print("What you want to order here is the menu")
        print(ad.show_menu())
        print("Enter the food ID to order to order the food")
        user_choice = int(input("If you want to order then select 1.YES 2.NO"))
        if user_choice == 1:
            foodid = int(input("Enter the food id here: "))
            quan = int(input("Enter the quantity of the food: "))
            x = ad.menu[foodid]["Price"] * quan
            again_ask = input("Are you still want to order this Enter YES or NO")
            if again_ask == "YES":
                print(f'''Your food name is {ad.menu[foodid]["Food Name"]}''')
                print(f'''Price of your food is {ad.menu[foodid]["Price"]}''')
                print(f"This is your quantity {quan}")
                print(f"It costs you {x}INR in total")
                print("You're all set for this order")
                self.order_history[foodid] = {
                    "Food Name": ad.menu[foodid]["Food Name"],
                    "Price": ad.menu[foodid]["Price"],
                    "Quantity": quan
                }
                final_stock = ad.menu[foodid]["Stock"] - quan
                ad.menu[foodid]["Stock"] = final_stock
                print("You're order is successfully placed")

            elif again_ask == "NO":
                print("This Order is cancelled!! You can look once more")
            else:
                print("Invalid choice")
        elif user_choice == 2:
            print("You select 2 option so we cancelled this")
        else:
            print("Enter the invalid choice")

    def watch_profile(self):
        print(self.profile)



Sajal = User("Sajal Tiwari", "9821049636", "sajaltiwari253@gmail.com", "93-Mayur Market", "Sajal@1234")
Nidhi = User("Nidhi Verma", "9406577715", "nidhiverma@gmail.com", "Gautam Nagar", "Nidhi@1234")
Sajal.see_profile()
Nidhi.see_profile()