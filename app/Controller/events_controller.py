import Data.Repository.events_repository as er
import Data.Repository.people_repository as pr


def add_event(event):
    return er.add_event(event)


def add_event_to_person(event, person):
    pr.add_event_to_person(event, person)


def show_events():
    return er.show_events()
