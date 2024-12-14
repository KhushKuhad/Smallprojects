alphabets = "abcdefghijklmnopqrstuvwxyz"

alphabet_list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

en_or_de=''
l1 = ['encode','decode']
while en_or_de not in l1:
    en_or_de = input("type 'encode' for encryption and 'decode' for decryption : ") #making sure user only enters 'encode' or 'decode as choice'

text = input("Enter your text : ").lower()#input for text to be encrypted or decrypted
shift = int(input("Enter shift number : "))#input for shift number


'''def encrypt(given_text,shift_no=0):                                                                     -------------------------|
    encrypted_str = ''                                                                                                              |
    for char in given_text: #                                                                                                       |
        if char in alphabet_list:                                                                                                   |
            if alphabet_list.index(char) + shift_no > 25:                                                                           |
                rev_pos = (alphabet_list.index(char) + shift_no-25) - 1                                                             |
                encrypted_str = encrypted_str + (alphabet_list[rev_pos])                                   -----#SEPARATE FUNCTION FOR ENCODE-----
            else:                                                                                                                   |
                encrypted_str = encrypted_str + (alphabet_list[alphabet_list.index(char) + shift_no])                               |        
        elif char == ' ':                                                                                                           |
            encrypted_str = encrypted_str + char                                                                                    |
    print(encrypted_str)                                                                                                            |

def decrypt(given_text,shift_no=0):                                                                                                 |
    decrypted_str = ''                                                                                                              |
    for char in given_text:                                                                                                         |
        if char in alphabet_list:                                                                                                   |
            decrypted_str = decrypted_str + (alphabet_list[alphabet_list.index(char) - shift_no])          -----#SEPARATE FUNCTION FOR DECODE-----
        elif char == ' ':                                                                                                           |
            decrypted_str = decrypted_str + ' '                                                                                     |
    print(decrypted_str)                                                                                   -------------------------|
'''                                                                                                         

def caeser(choice,given_text,shift_no):
    final_text = ''
    if choice == 'decode':
        shift_no = shift_no * -1
    for char in given_text:
        if char in alphabet_list:
            if alphabet_list.index(char) + shift_no > 25:
                position = (alphabet_list.index(char) + shift_no-25) - 1  # FUNCTION 2 IN 1
            else:
                position = alphabet_list.index(char) + shift_no
            final_text = final_text + alphabet_list[position]
        elif char == ' ':
            final_text = final_text + ' '
    print(final_text)

caeser(en_or_de,text,shift)
