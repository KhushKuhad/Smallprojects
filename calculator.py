from os import system
calc = '''
_______________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''
def clear():
    system('cls')
#DEFINING OPERATIONS
def add(a,b): #MAKINF FUNCTIONS FOR EACH OPERATION
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
op_dict = {'+':add,'-':subtract,'/':divide,'*':multiply} #DICT OF EACH OPERATION AND SYMBOL
usage = True # WILL USE TO DECIDE THE END OF LOOP
num1 = '' #ASSIGNED TO str so that next loops can be ran 
while usage == True:
    print(calc)
    if type(num1)== str:
        num1 = float(input("Enter 1st num : ")) #IF num1 != str -> loop is re running
    else:
        print(f"Operation will be performed on {num1}")
    operation = ''
    while operation not in list(op_dict.keys()):#INPUT FOR OPERATION
        operation = input("what operation will u perform (+ , -, *, /) : ")
    num2 = float(input("enter another number to perform operation with : ")) #INPUT FOR ANOTHER NUMBER
    result = op_dict[operation](num1,num2) #PERFORMING OPERATION OF CHOICE AND ASSIGN IT TO RESULT
    print(f"{num1} {operation} {num2} = {result}") #PRINTIN OPERATION
    cont = ''
    while cont not in ['yes','no','new']:
        cont = input("would u like to continue (yes/no) or start a new calculation(new): ") #ASKING IF TO CONTINUE OR NOT OR START A NEW CALCULATION
    clear()
    if cont == 'yes':
        num1 = result #TO RE RUN THE LOOP
    elif cont == 'new':
        num1 = ''
    else:
        usage = False #TERMINATION OF WHILE LOOP
