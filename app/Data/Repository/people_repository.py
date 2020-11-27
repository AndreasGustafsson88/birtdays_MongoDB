from Data.Models.people import People
from Data.Models.user import User


def show_all_people():
    return People.all()


def update_people():
    return


def exists(people):
    return People.find(dob=people.dob).exists()


def save_people(new_people):
    failed = []
    master = User.find().first_or_none()
    for people in new_people:
        try:
            people.save()
            master.people.append(people._id)
            master.save()
        except:
            failed.append(people)
            continue

    return failed if len(failed) > 0 else True


def find_person(search):
    return People.find(first_name=search).first_or_none()


def add_event_to_person(event, person):
    person.events.append(event)
    person.save()

