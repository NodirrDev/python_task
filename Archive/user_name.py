import random

def user_name():
    username = input("Ismingizni kiriting: ")


    username = username.lower()[::-1]
    ran_number = random.randint(0,9)

    username = username + str(ran_number)
    return username

print('hello')







