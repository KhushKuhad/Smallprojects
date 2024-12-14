choice = ''
while choice not in [1,2,3,4,5]:
    choice = int(input("1 - espresso( 45$ )\n2 - latte(  65$ )\n3 - cappuccino( 100$ )\n4 - report\n5 - Off\nENTER CHOICE : "))

class coffee_machine:
    def __init__(self,milk=300,water=300,coffee=100,money=0):
        self.milk = milk
        self.water = water
        self.coffee = coffee
        self.money = money

    def machine_contents(self):
        print(f"milk : {self.milk}ml\nwater : {self.water}ml\ncoffee : {self.coffee}g\nmoney : {self.money}$")
    
    def check_for_sufficient_resources(self,choice):
        if choice == 1:
            if self.water >= 50 and self.coffee >= 18:
                return True
            else:
                return False
        elif choice == 2:
            if self.water >= 50 and self.coffee >= 24 and self.milk >= 100:
                return True
            else:
                return False
        elif choice == 3:
            if self.water >= 50 and self.coffee >= 24 and self.milk >= 150:
                return True
            else:
                return False

    def make_coffee(self,choice):
        change = 0
        while change not in range(1,999999):
            change = int(input("Enter amount to pay : "))

        if change >= [45,65,100][choice-1]:
            if choice == 1:
                self.water = self.water - 50
                self.coffee =self.coffee - 18
                self.money = self.money + 45
            elif choice == 2:
                self.water = self.water - 50
                self.milk = self.milk - 100
                self.coffee = self.coffee - 24
                self.money = self.money + 65
            else:
                self.water = self.water - 50
                self.milk = self.milk - 150
                self.coffee = self.coffee - 24
                self.money = self.money + 100
            if change > [45,65,100][choice-1]:
                print(f"Enjoy Your Coffee\nHere is your change : {change-[45,65,100][choice-1]}")                
            elif change == [45,65,100][choice-1]:
                print("Enjoy Your Coffee")
                return True
        else:
            print("bhikari!!")
            return False

a = coffee_machine()
while True:
    if choice == 4:
        a.machine_contents()
    elif choice == 5:
        print("BYE")
        break
    else:
        if a.check_for_sufficient_resources(choice=choice):
            if a.make_coffee(choice=choice) == False:
                break
        else:
            print("Machine does not have sufficient resources")
            break
    choice = ''
    while choice not in [1,2,3,4,5]:
        choice = int(input("1 - espresso( 45$ )\n2 - latte(  65$ )\n3 - cappuccino( 100$ )\n4 - report\n5 - Off\nENTER CHOICE : "))