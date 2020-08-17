import random
# Write your code here


def card_generator():
    global card
    card = '400000'
    i = 0
    while i < 10:
        card_number = random.choice('0123456789')
        card += card_number
        i += 1
    print("Your card number:\n", card, sep="")


def pin_generator():
    global pin
    pin = ''
    i = 0
    while i < 4:
        pin_number = random.choice('0123456789')
        pin += pin_number
        i += 1
    print("Your card PIN:\n", pin, "\n", sep="")


def check():
    card_inp = input("\nEnter your card number:\n")
    pin_inp = input("Enter your PIN:\n")
    if (card_inp == card) and (pin_inp == pin):
        print("\nYou have successfully logged in!\n")
        show_balance()
    else:
        print("\nWrong card number or PIN!\n")


def show_balance():
    while True:
        print("1. Balance\n2. Log out\n0. Exit")
        when_logged_inp = int(input())
        if when_logged_inp == 1:
            print("\nBalance: 0\n")
        elif when_logged_inp == 2:
            print("\nYou have successfully logged out!\n")
            break
        elif when_logged_inp == 0:
            print("Bye!")
            exit(0)


while True:
    user_inp = input("1. Create an account\n2. Log into account\n0. Exit\n")
    if user_inp == '1':
        print("\nYour card has been created")
        card_generator()
        pin_generator()
        continue
    elif user_inp == '2':
        check()
        continue
    elif user_inp == '0':
        print("\nBye!")
        break
