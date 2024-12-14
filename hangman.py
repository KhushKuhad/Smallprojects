from random import randint
import os
clear = lambda:os.system('cls') #to clear screen
word_list = ['remember','introduction','communication','hostility','circulation','reservoir','integrity','reconcile','literacy','hemisphere','decrease','discriminate','charismatic','verdict','referral','examination','intervention','elegant','invasion','accountant','alcohol','regular','technique','freckle','reactor','sentence','executive','evening','residence','physics',"tablet","chairs","paper","variety"]
#list of words(randomly chosen)
word = word_list[randint(0,len(word_list)-1)] #choosing a random word
empty_word=''
for letter in word:
    empty_word = empty_word+'_ ' #creating "_ _ _ _ _" display for unguessed letters
unfinalized_str=empty_word
list_unfinalized_str = unfinalized_str.split() #

#hangman drawings to display if guess goes wrong
HANGMANPICS = ["               ",'''
      |
      |
      |
      |
      |
=========''', '''
  +---+
      |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  | 
=========''']
print(empty_word)
tries=0 #will be used to terminate the while loop
while tries <9:

    guess = ''
    while guess.isalpha()==False and len(guess)==0:
        guess = input("Enter your guess : ").lower()[0] #making sure the guess is a single alphabtet
    clear() #clearing output
    if guess not in word:
        tries = tries+1 #if wrong guess
    i=0

    l1=empty_word.split()
    for letter in word:
        if guess == letter:
            l1[i]=guess #creating a list of all characters in the word
        i=i+1
    print(HANGMANPICS[tries]) #will print hangman according to the number of errors

    if guess in list_unfinalized_str:
        print(f"You already guessed '{guess}' !!!!!!!!")#if letter already guessed

    updated_str=''
    for char in l1:
        updated_str=updated_str+char+' '
    n=0
    for char in l1:
        if char.isalpha():
            list_unfinalized_str[n] = updated_str[n*2]
        n=n+1 # creation of unfinalized_str before printing

    final_str=''
    for char in list_unfinalized_str:
        final_str = final_str+char+' ' #creating final_str which will be displayed
    print(final_str) #OUTPUT str
    if '_' not in list_unfinalized_str:
        print("YOU WIN")
        break #WIN CHECK
if tries==9:
    print("YOU LOST") #LOSS CHECK
    print(f"The word was {word}")