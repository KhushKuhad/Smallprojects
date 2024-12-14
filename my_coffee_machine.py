user_choice = ''
while user_choice not in ['1','2','3','report','off']:
    user_choice = (input("what would you like? (espresso( 1 )/latte( 2 )/cappucino( 3 ))\n 'off' to exit 'report' to see report  : "))

try: #converting choice to int for order number
    user_choice = int(user_choice)
except:
    pass

if user_choice == 1: #aligning order number and item name 
    order = 'espresso'
elif user_choice == 2:
    order = 'latte'
elif user_choice == 3:
    order = 'cappuccino'

machine_contents = {'milk': 200,'coffee':100,'water':300,'money':0} #machine ingridients
menu = [[50,18],[100,24,150],[150,24,100]] #ingridients required for each coffee

requirements = [{'espresso':[50,18,45]},{'latte':[100,24,150,65]},{'cappuccino':[150,24,150,110]}] #dictionaries of coffee name and ingridients
def print_machine_contents():
    '''Reports the machine contents'''
    lst = ['milk','water','coffee','money']
    lst2 = ['ml','ml','g','$']
    for num in range(0,4): #printing the ingridients
        print(f"{lst[num]} - {machine_contents[lst[num]]}{lst2[num]}")

def check_resources(): #True if resources enough, False if not enough
    '''cross checking whether resources are enough for the item ordered'''
    n=0
    for num in range(0,len(menu[user_choice-1])):
        if machine_contents[list(machine_contents.keys())[num]] >= menu[user_choice-1][num]:
            n = n+1
            if n == len(menu[user_choice-1]):
                return True
            else:
                pass
        else:
            return False

def deduct_resources(): #deducts resources after payment validation
    '''code for deduction of resources for the order'''
    if order == 'espresso':
        machine_contents['water'] = machine_contents['water'] - 50
        machine_contents['coffee'] = machine_contents['coffee'] - 18
    else:
        if order == 'latte':
            req_milk = 100
        else:
            req_milk = 150
        machine_contents['milk'] = machine_contents['milk'] - req_milk
        machine_contents['water'] = machine_contents['water'] - 150
        machine_contents['coffee'] = machine_contents['coffee'] - 24

def take_payment():
    '''validating payments, returns change and deduction of resource'''
    print(f"To pay : {requirements[user_choice-1][order][-1]}")
    fives = int(input("How many fives : "))
    fives = fives*5
    tens = int(input("How many tens : " ))
    tens = tens*10
    twenties = int(input("How many twenties : "))
    twenties = twenties*20
    total = fives+tens+twenties
    if total >= requirements[user_choice-1][order][-1]:
        change = total - requirements[user_choice-1][order][-1]
        print(f"Your change : {change},\nENJOY YOUR COFFEE")
        machine_contents['money'] = machine_contents['money'] + requirements[user_choice-1][order][-1]
        deduct_resources()
        return True
    elif total < requirements[user_choice-1][order][-1]:
        print("BROKIE!")
        return False

while True:
    if user_choice == 'off':
        break
    elif user_choice == 'report':
        print_machine_contents()
    else:
        if check_resources() == False:
            print("LOW ON RESOURCES")
            print_machine_contents()
            break
        else:
            a = take_payment()
            if a == False:
                print("Try again with sufficient money")
    user_choice = ''
    while user_choice not in ['1','2','3','report','off']:
        user_choice = (input("what would you like? (espresso( 1 )/latte( 2 )/cappucino( 3 ))\n 'off' to exit 'report' to see report  : "))
    try:
        user_choice = int(user_choice)
    except:
        pass
    if user_choice == 1:
        order = 'espresso'
    elif user_choice == 2:
        order = 'latte'
    elif user_choice == 3:
        order = 'cappuccino'