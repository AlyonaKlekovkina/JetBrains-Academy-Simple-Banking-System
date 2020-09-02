import random
import math
import sqlite3

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute("CREATE TABLE if not exists card (id INTEGER, number TEXT, pin TEXT, balance INTEGER default'0');")


def luhn_algorithm(card_to_be_checked):
    multiplied_by_two = []
    for i in range(len(card_to_be_checked)):
        if i % 2 == 0:
            multiplied_by_two.append(int(card_to_be_checked[i]) * 2)
        else:
            multiplied_by_two.append(int(card_to_be_checked[i]))
    for i in range(len(multiplied_by_two)):
        if multiplied_by_two[i] > 9:
            multiplied_by_two[i] = multiplied_by_two[i] - 9
    result = sum(multiplied_by_two)
    return result


def card_generator():
    card = '400000'
    for i in range(9):
        card_number = random.choice('0123456789')
        card += card_number
    checksum = luhn_algorithm(card)
    if checksum % 10 == 0:
        last_digit = '0'
    else:
        nearest_tenth = int(math.ceil(checksum / 10.0)) * 10
        last_digit = str(nearest_tenth - checksum)
    final_card_number = card + last_digit
    return final_card_number


def pin_generator():
    the_pin = ''
    for i in range(4):
        pin_number = random.choice('0123456789')
        the_pin += pin_number
    return the_pin


def check_card_pin_number():
    global logged_in_card
    card_inp = input("\nEnter your card number:\n")
    pin_inp = input("Enter your PIN:\n")
    card_query = "SELECT Count(*) FROM card WHERE number = '{}' AND pin = '{}'".format(card_inp, pin_inp)
    cur.execute(card_query)
    card_records = cur.fetchone()
    returned_count = card_records[0]
    if returned_count == 1:
        logged_in_card = card_inp
        print("\nYou have successfully logged in!\n")
        show_menu()
    else:
        print("\nWrong card number or PIN!\n")


def get_balance(card_number):
    balance_query = "SELECT balance FROM card WHERE number = {}".format(card_number)
    cur.execute(balance_query)
    records = cur.fetchone()
    balance = records[0]
    return balance


def existing_cards():
    cards_query = "SELECT number from card"
    cur.execute(cards_query)
    all_cards = [i[0] for i in cur.fetchall()]
    return all_cards


def add_income(input_from_user):
    current_balance = get_balance(logged_in_card)
    updated_income = current_balance + input_from_user
    update_income_statement = "UPDATE card SET balance = {} WHERE number = {}".format(updated_income, logged_in_card)
    cur.execute(update_income_statement)
    conn.commit()


def make_transfer_from():
    card_balance_from = get_balance(logged_in_card)
    amount_after_transfer_from = card_balance_from - transfer_amount
    transfer_from_statement = "UPDATE card SET balance = {} WHERE number = {}".format(amount_after_transfer_from, logged_in_card)
    cur.execute(transfer_from_statement)
    conn.commit()


def make_transfer_to():
    card_balance_from = get_balance(transfer_card_inp)
    amount_after_transfer_to = card_balance_from + transfer_amount
    transfer_to_statement = "UPDATE card SET balance = {} WHERE number = {}".format(amount_after_transfer_to, transfer_card_inp)
    cur.execute(transfer_to_statement)
    conn.commit()


def show_menu():
    global transfer_card_inp, transfer_amount
    while True:
        print("1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit")
        when_logged_inp = int(input())
        if when_logged_inp == 1:
            print("Balance:", get_balance(logged_in_card))
        elif when_logged_inp == 2:
            income_inp = int(input("Enter income:\n"))
            add_income(income_inp)
            print("Income was added!")
        elif when_logged_inp == 3:
            the_cards = existing_cards()
            transfer_card_inp = input("Transfer\nEnter card number:\n")
            transfer_card_result = luhn_algorithm(transfer_card_inp)
            if transfer_card_result % 10 != 0:
                print("Probably you made mistake in the card number. Please try again!\n")
            elif transfer_card_inp not in the_cards:
                print("Such a card does not exist.\n")
            elif transfer_card_inp == logged_in_card:
                print("You can't transfer money to the same account!\n")
            else:
                transfer_amount = int(input("Enter how much money you want to transfer:\n"))
                current_balance = get_balance(logged_in_card)
                if transfer_amount > current_balance:
                    print("Not enough money!\n")
                else:
                    make_transfer_from()
                    make_transfer_to()
                    print("Success!")
        elif when_logged_inp == 4:
            delete_statement = "DELETE from card where number = {}".format(logged_in_card)
            cur.execute(delete_statement)
            conn.commit()
            cur.close()
            print("The account has been closed!")
            break
        elif when_logged_inp == 5:
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
        insert_card_pin_statement = "INSERT INTO card (number, pin) VALUES ('{}', '{}')".format(number, pin)
        cur.execute(insert_card_pin_statement)
        conn.commit()
        continue
    elif user_inp == '2':
        check_card_pin_number()
        continue
    elif user_inp == '0':
        print("\nBye!")
        break
