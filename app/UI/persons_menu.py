from Controller.helper_functions import int_input_verification
import Controller.persons_controller as pc


def persons_menu():
    while True:
        print("Persons menu".center(40))
        print("=".center(40, "="), "\n")

        print("1. Show people")
        print("2. Update people")
        print("0. Back\n")

        selection = int_input_verification()

        if selection == 1:
            pc.show_all_people()

        elif selection == 2:
            pc.update_people()

        elif selection == 0:
            break
