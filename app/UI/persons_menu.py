from Controller.helper_functions import int_input_verification
import Controller.persons_controller as pc


def update_menu():
    new_people = pc.update_people()

    if len(new_people) > 0:
        for i, people in enumerate(new_people, 1):
            print(f"{i}".center(40, "-"))
            print(people)
            print()

        print("Are you happy with these changes?\n(1) Yes\n(2) No")

        selection = int_input_verification()

        if selection == 1:
            saved = pc.save_people(new_people)
            if isinstance(saved, bool):
                print(f"Save successful!".center(40, " "))

            else:
                print(f"{saved} wasn't saved")

        elif selection == 2:
            print("Save cancelled!".center(40, " "))

    else:
        print("Everyting is up to date!".center(40, " "))


def persons_menu():
    while True:
        print("Persons menu".center(40))
        print("=".center(40, "="), "\n")

        print("1. Show people")
        print("2. Update people")
        print("0. Back\n")

        selection = int_input_verification()

        if selection == 1:
            people = pc.show_all_people()
            print("\n".join(f"{i}.\n{person.first_name} {person.last_name}\n---{person.relation}---\n"
                            for i, person in enumerate(people, 1)))

        elif selection == 2:
            update_menu()

        elif selection == 0:
            break
