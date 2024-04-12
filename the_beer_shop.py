class Beer:
    def __init__(self, brand, full_vol, current_vol, strength, amount, is_open=False):
        self.brand = brand
        self.full_vol = full_vol
        self.current_vol = current_vol
        self.strength = strength
        self.is_open = is_open
        self.amount = amount

    def opening(self):
        if not self.is_open:
            print("Opening the can.")
            self.is_open = True
        else:
            print("It's already opened.")

    def drinking(self):
        if self.is_open:
            if self.current_vol != 0:
                self.amount = int(input("How much do you want to drink?\n"))
                if self.current_vol >= self.amount:
                    print("Drinking the water...")
                    self.current_vol = self.current_vol - self.amount
                    print(f"There is {self.current_vol}ml left.")
                else:
                    print("That's too much! There is not enough in the can.")
            else:
                print("The can is empty!")
        else:
            print("You have to open the can!")

    def presentation(self):
        print(f"Full Volume: {self.full_vol} ml")
        print(f"Current Volume: {self.current_vol} ml")
        print(f"Is Open: {'Yes' if self.is_open else 'No'}")

    def what_beer(self):
        print(f"The brand of the beer: {self.brand}.")
        print(f"The volume of the beer: {self.full_vol} ml.")
        print(f"The strength of the beer: {self.strength}.")

    def buy_new(self):
        self.current_vol = self.full_vol
        print(f"You just bought a brand new can of {self.brand} beer!")
        self.is_open = False


beer1 = Beer(brand="Żywiec", full_vol=500, current_vol=500, strength=4, amount=0, is_open=False)
beer2 = Beer(brand="Tyskie", full_vol=450, current_vol=450, strength=5, amount=0, is_open=False)
beer3 = Beer(brand="Smakowe", full_vol=600, current_vol=600, strength=2, amount=0, is_open=False)
beer4 = Beer(brand="EKO", full_vol=550, current_vol=550, strength=1, amount=0, is_open=False)

print("Hello! Welcome to the Beer Store.")
print("")
while True:
    option1 = input("What beer do you want to learn about? 1, 2, 3, or 4?\nAre you read to choose? (5)\n")
    if option1 == "1":
        beer1.what_beer()
        print("")
    elif option1 == "2":
        beer2.what_beer()
        print("")
    elif option1 == "3":
        beer3.what_beer()
        print("")
    elif option1 == "4":
        beer4.what_beer()
        print("")
    elif option1 == "5":
        break
    else:
        print("There is no beer like that.")
print("")
option2 = input("What beer do you want to choose? 1, 2, 3 or 4?\n")
if option2 == "1":
    print("You just bought the Żywiec beer.")
    option2 = beer1
    print("")
elif option2 == "2":
    print("You just bought the Tyskie beer.")
    option2 = beer2
    print("")
elif option2 == "3":
    print("You just bought the Smakowe beer.")
    option2 = beer3
    print("")
elif option2 == "4":
    print("You just bought the EKO beer.")
    option2 = beer4
    print("")
else:
    print("There is no beer like that.")

print("")
while True:
    option3 = input("What do you want to do?\n1.Drink\n2.Open\n3.Buy a new one\n4.Read info\n5. Leave\n")
    option3 = int(option3)
    if option3 == 1:
        option2.drinking()
    elif option3 == 2:
        option2.opening()
    elif option3 == 3:
        option2.buy_new()
    elif option3 == 4:
        option2.what_beer()
        option2.presentation()
    elif option3 == 5:
        break
    else:
        break
