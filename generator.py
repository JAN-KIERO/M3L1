import random

def gen():
    letters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    number = 8
    password = ""

    for i in range(number):
        password += random.choice(letters)
        
    return password
        