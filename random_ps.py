import random

def generate_password(pwd_length):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    passwords = []

    for i in pwd_length:
        password = ""
        for j in range(i):
            next_letter_index = random.randrange(len(alphabet))
            password = password + alphabet[next_letter_index]
            #what could be generated 
        password = replace_with_number(password)
        password = replace_with_uppercase_letter(password)

        password.append(password)