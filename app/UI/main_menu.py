from Controller.helper_functions import int_input_verification
from UI.events_menu import events_menu
from UI.gift_menu import gifts_menu
from UI.persons_menu import persons_menu


def main_menu():
    while True:
        print("Welcome to the events calendar".center(40, "-"))
        print("=".center(40, "="), "\n")

        print("1. Persons")
        print("2. Gifts")
        print("3. Events")
        print("0. Quit\n")

        selection = int_input_verification()

        if selection == 1:
            persons_menu()

        elif selection == 2:
            gifts_menu()

        elif selection == 3:
            events_menu()

        elif selection == 0:
            break
