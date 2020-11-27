from Controller.helper_functions import int_input_verification
import Controller.gifts_controller as gc
import Controller.persons_controller as pc
from Data.Models.events import Event


def check_for_event(person):
    if len(person.events) != 0:
        print("Is this gift for any of these events?")
        print("0. to exit")
        print("\n".join(f"{i}. {event['description']}" for i, event in enumerate(person.events, 1)))

        selection = int_input_verification()

        if selection == 0:
            return True

        return Event.find(description=person.events[selection - 1]["description"]).first_or_none()

    else:
        print(f"No events found for {person.first_name}")
        return True


def add_gift_to_event(gift):
    while True:
        search = input("Who is gift for?\n> ")

        person = pc.find_person(search)

        print(f"{person.first_name} {person.last_name} who is your {person.relation}")

        print("Is this correct?\n(1) Yes\n(2) No, search again\n(3) Exit")
        selection = int_input_verification()

        if selection == 1:
            event = check_for_event(person)
            if event:
                gift = gc.add_gift(gift)
                print(f"Gift {gift.name} has been saved")
                break

            else:
                gift = gc.add_gift(gift)
                gc.add_gift_to_event(event, gift)
                print(f"Gift {gift.name} has been saved and added to {event.description}")
                break

        if selection == 2:
            continue

        if selection == 3:
            break


def add_gifts_menu():
    while True:
        print("Add gifts menu".center(40, "-"))
        print("=".center(40, "="), "\n")

        gift = {f"{i.replace(' ', '_').lower()}": input(f"{i}: ") for i in
                ["Name", "Description", "Link", "Price"]}

        print("OBS".center(40, "-"))
        print("\n".join(f"{k} = {v}" for k, v in gift.items()))

        print("is the information correct?\n(1) Yes\n(2) No")
        selection = int_input_verification()

        # TODO add feature to add to event or create event here! or adding custom fields

        if selection == 1:
            add_gift_to_event(gift)
            break

        elif selection == 2:
            break


def gifts_menu():
    while True:
        print("Gifts menu".center(40, "-"))
        print("=".center(40, "="), "\n")

        print("1. Show gifts")
        print("2. Add gifts")
        print("0. Back\n")

        selection = int_input_verification()

        if selection == 1:
            # TODO add show gifts that hasn't been connected to an event yet
            all_gifts = gc.show_gifts()
            print("\n".join(f"\n---{i}. {gift.description}---\n{gift.name}\nPrice: {gift.price},-\n"
                            for i, gift in enumerate(all_gifts, 1)))

        elif selection == 2:
            add_gifts_menu()

        elif selection == 0:
            break
