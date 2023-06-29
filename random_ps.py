import random

def generate_password(pwd_length):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    passwords = []

    for i in pwd_length:
        password = ""