import Data.Repository.gifts_repository as gr
import Data.Repository.events_repository as er


def add_gift(gift):
    return gr.add_gifts(gift)


def show_gifts():
    return gr.show_gifts()


def add_gift_to_event(event, gift):
    er.add_gift_to_event(event, gift)
