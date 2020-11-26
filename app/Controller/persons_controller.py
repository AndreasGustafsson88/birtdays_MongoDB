import Data.Repository.people_repository as pr
from Data.Models.people import People


def show_all_people():
    pr.show_all_people()


def update_people():
    with open("C:/Kod/Projekt/Birthdays/Birtdays MongoDB/_documents/people.txt") as file:
        all_people = []
        for column in file.readlines():
            line = column.split()
            people = {
                "first_name": line[0],
                "last_name": line[1],
                "dob": line[2],
                "relation": line[3]
            }
            if not pr.exists(people):
                all_people.append(People(people))

    for people in all_people:
        print(people)

    pr.update_people()
