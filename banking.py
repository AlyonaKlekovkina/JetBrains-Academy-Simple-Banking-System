import random
import math
import sqlite3
# Write your code here
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute("CREATE TABLE if not exists card (id INTEGER, number TEXT, pin TEXT, balance INTEGER default'0');")


def card_generator():
    card = '400000'
    for i in range(9):
        card_number = random.choice('0123456789')
        card += card_number

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
    return final_card_number


def pin_generator():
    the_pin = ''
    for i in range(4):
        pin_number = random.choice('0123456789')
        the_pin += pin_number
    return the_pin


def check():
    card_inp = input("\nEnter your card number:\n")
    pin_inp = input("Enter your PIN:\n")
    if (card_inp == number) and (pin_inp == pin):
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
        number = card_generator()
        print("Your card number:\n", number, sep="")
        pin = pin_generator()
        print("Your card PIN:\n", pin, "\n", sep="")
        insert_sql_statement = "INSERT INTO card (number, pin) VALUES ({}, {})".format(number, pin)
        cur.execute(insert_sql_statement)
        conn.commit()
        continue
    elif user_inp == '2':
        check()
        continue
    elif user_inp == '0':
        print("\nBye!")
        break
