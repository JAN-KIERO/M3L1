import random

def gen(number):
    letters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    password = ""

    for i in range(number):
        password += random.choice(letters)
        
    return password
        