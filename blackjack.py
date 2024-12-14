import random
from os import system
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':1}
suits = ('Hearts','Spades','Diamonds','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')

def clear():
    system('cls')
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                
                self.all_cards.append(created_card)
    def shuffle_deck(self):
        random.shuffle(self.all_cards)
        
    def remove_one(self):
        return self.all_cards.pop(0)

class Player:
    def __init__(self,name,balance=100,a_list = []):
        self.name = name
        self.balance = balance
        self.a_list = a_list
        
    def Deposit(self,dep_amount):
        self.balance = self.balance + dep_amount
        
    def Withdraw_lost(self,with_amount):
        self.balance = self.balance - with_amount

new_deck = Deck()
new_deck.shuffle_deck()

def show_dealer_cards():
    if len(dealer_hand_cards) == 0:
        print("EMPTY HAND")
    else:
        for i in range(0,len(dealer_hand_cards)):
            print(dealer_hand_cards[i])

def show_your_cards():
    if len(your_hand_cards_list) == 0:
        print('Empyt hand')
    else:
        for i in range(0,len(your_hand_cards_list)):
            print(your_hand_cards_list[i])

def show_card_value():
    a = 0
    for element in range(0, len(your_hand_cards_list)):
        a = a + your_hand_cards_list[element].value
    return a

def show_dealer_value():
    a = 0
    for  element in range(0,len(dealer_hand_cards)):
        a = a + dealer_hand_cards[element].value
    return a

def win_check():
    a = 0
    b = 0
    for element in range(0, len(your_hand_cards_list)):
        a = a + your_hand_cards_list[element].value
    
    for element in range(0,len(dealer_hand_cards)):
        b = b + dealer_hand_cards[element].value
        
    if a == 21:
        print('BLACKJACK!!')
        winn = True
        
    elif b == 21:
        print('You Lose!')
        winn = True
    elif b > 21:
        print('Dealer BUSTED, YOU WIN')
        winn = True
    elif a > 21:
        print('BUSTED')
        winn = True
    else:
        winn = False
    return winn

def win_check_rounds():
    winnn = False
    a = 0
    b = 0
    for element in range(0, len(your_hand_cards_list)):
        a = a + your_hand_cards_list[element].value

    for element in range(0,len(dealer_hand_cards)):
        b = b + dealer_hand_cards[element].value

    if abs(21-a) < abs(21-b):
        print('YOU WIN')
        winnn = True
    elif abs(21-a) > abs(21-b):
        print('YOU LOSE')
        winnn = True
    else:
        winnn = False
    return winnn

def hit_or_stand():
    ans = ''
    while ans not in ['H','S','h','s']:
        ans = input('enter H for hit and S for stand: ')
    return ans

def hit():
    if len(your_hand_cards_list_1) != 0 and len(dealer_hand_cards_1) != 0:
        your_hand_cards_list.append(your_hand_cards_list_1.pop(0))
        dealer_hand_cards.append(dealer_hand_cards_1.pop(0))
        
    elif len(your_hand_cards_list_1) != 0 and len(dealer_hand_cards_1) == 0:
        your_hand_cards_list.append(your_hand_cards_list_1.pop(0))

def stand():
    if len(dealer_hand_cards_1) != 0:
        dealer_hand_cards.append(dealer_hand_cards_1.pop(0))

new_deck = Deck()
new_deck.shuffle_deck()
player = Player('player')
dealer_hand_cards = []
dealer_hand_cards_1 = []
def dealer_hand():
    while len(dealer_hand_cards_1) != 4:
        dealer_hand_cards_1.append(new_deck.remove_one())
dealer_hand()
your_hand_cards_list = []
your_hand_cards_list_1 = []
def your_hand_cards():
    while len(your_hand_cards_list_1) != 4:
        your_hand_cards_list_1.append(new_deck.remove_one())
your_hand_cards()
##DEALER HAND
dealer_hand_cards.insert(0,dealer_hand_cards_1.pop(0))

##YOUR HAND
your_hand_cards_list.insert(0,your_hand_cards_list_1.pop(0))
your_hand_cards_list.insert(0,your_hand_cards_list_1.pop(0))
game_on  = True
win_game = False
while game_on:
    clear()
    if win_game == True:
        game_on = False
        break
    print('________DEALER hand________')
    show_dealer_cards()
    dealer_value = show_dealer_value()
    print(dealer_value)
    print('________YOUR hand________')
    show_your_cards()
    your_value = show_card_value()
    print(your_value)
    choice = hit_or_stand()
    if choice in ['h','H']:
        hit()
        print('________DEALER hand________')
        show_dealer_cards()
        dealer_value = show_dealer_value()
        print(dealer_value)
        print('________YOUR hand________')
        show_your_cards()
        your_value = show_card_value()
        print(your_value)
        if win_check() == True:
            break
        else:
            continue
    else:
        stand()
        print('________DEALER hand________')
        show_dealer_cards()
        dealer_value = show_dealer_value()
        print(dealer_value)
        print('________YOUR hand________')
        show_your_cards()
        your_value = show_card_value()
        print(your_value)
        win_check_rounds()
        break