import random

def gen_pass():
    source = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    password_lenght = 10
    password = ""

    for i in range(password_lenght):
        password += random.choice(source)

    return password