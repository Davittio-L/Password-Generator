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

    return passwords

def replace_with_number(pwd_word):
    for i in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pwd_word)//2)
        pwd_word = pwd_word[0: replace_index] + pwd_word[replace_index].upper() + pwd_word[replace_index + 1]
        return pwd_word

def replace_with_uppercase_letter(pwd_word):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2,len(pword))
        pwd_word = pwd_word[0:replace_index] + pwd_word[replace_index].upper() + pwd_word[replace_index+1:]
        return pwd_word