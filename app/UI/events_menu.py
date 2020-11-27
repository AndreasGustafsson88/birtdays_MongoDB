from Controller.helper_functions import int_input_verification
import Controller.events_controller as ec
import Controller.persons_controller as pc


def add_person_to_event(event):
    while True:
        search = input("Who is this event for?\n> ")

        person = pc.find_person(search)

        print(f"{person.first_name} {person.last_name} who is your {person.relation}")

        print("Is this correct?\n(1) Yes\n(2) No, search again\n(3) Exit")
        selection = int_input_verification()

        if selection == 1:
            happening = ec.add_event(event)
            ec.add_event_to_person(event, person)
            print(f"Event {happening.description} has been saved for {person.first_name}")
            break

        if selection == 2:
            continue

        if selection == 3:
            break


def add_events_menu():
    while True:
        print("Add events menu".center(40, "-"))
        print("=".center(40, "="), "\n")

        event = {f"{i.replace(' ', '_').lower()}": input(f"{i}: ") for i in
                 ["Name", "Description", "Date", "Location"]}

        event.update({"gifts": []})

        print("OBS".center(40, "-"))
        print("\n".join(f"{k} = {v}" for k, v in event.items()))

        print("is the information correct?\n(1) Yes\n(2) No")
        selection = int_input_verification()

        if selection == 1:
            add_person_to_event(event)
            break

        elif selection == 2:
            break


def events_menu():
    while True:
        print("Events menu".center(40, "-"))
        print("=".center(40, "="), "\n")

        print("1. Show events")
        print("2. Add event")
        print("0. Back\n")

        selection = int_input_verification()

        if selection == 1:
            events = ec.show_events()
            print("\n".join(f"{event.description} on {event.date}" for event in events))

        elif selection == 2:
            add_events_menu()
            break

        elif selection == 0:
            break
