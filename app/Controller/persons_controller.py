import Data.Repository.people_repository as pr
from Data.Models.people import People


def show_all_people():
    return pr.show_all_people()


def update_people():
    with open("C:/Kod/Projekt/Birthdays/Birtdays MongoDB/_documents/people.txt") as file:
        all_people = []
        for column in file.readlines():
            line = column.split()
            people = {
                "first_name": line[0],
                "last_name": line[1],
                "dob": line[2],
                "relation": line[3],
                "events": []
            }
            person = People(people)
            if not pr.exists(person):
                all_people.append(person)

    return all_people


def save_people(new_people):
    return pr.save_people(new_people)


def find_person(search):
    return pr.find_person(search)
