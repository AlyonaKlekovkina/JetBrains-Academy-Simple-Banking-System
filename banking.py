import random
import math
# Write your code here


def card_generator():
    global card
    card = '400000'
    for i in range(9):
        card_number = random.choice('0123456789')
        card += card_number


def checksum():
    global last_digit, final_card_number
    multiplied_by_two = []
    for i in range(len(card)):
        if i % 2 == 0:
            multiplied_by_two.append(int(card[i]) * 2)
        else:
            multiplied_by_two.append(int(card[i]))

    for i in range(len(multiplied_by_two)):
        if multiplied_by_two[i] > 9:
            multiplied_by_two[i] = multiplied_by_two[i] - 9
    result = sum(multiplied_by_two)

    if result % 10 == 0:
        last_digit = '0'
    else:
        nearest_tenth = int(math.ceil(result / 10.0)) * 10
        last_digit = str(nearest_tenth - result)
    final_card_number = card + last_digit
    print("Your card number:\n", final_card_number, sep="")


def pin_generator():
    global pin
    pin = ''
    for i in range(4):
        pin_number = random.choice('0123456789')
        pin += pin_number
    print("Your card PIN:\n", pin, "\n", sep="")


def check():
    card_inp = input("\nEnter your card number:\n")
    pin_inp = input("Enter your PIN:\n")
    if (card_inp == final_card_number) and (pin_inp == pin):
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
            break


while True:
    user_inp = input("1. Create an account\n2. Log into account\n0. Exit\n")
    if user_inp == '1':
        print("\nYour card has been created")
        card_generator()
        checksum()
        pin_generator()
        continue
    elif user_inp == '2':
        check()
        continue
    elif user_inp == '0':
        print("\nBye!")
        break
