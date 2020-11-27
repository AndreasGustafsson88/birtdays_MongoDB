from Data.Models.events import Event


def add_event(event):
    happening = Event(event)
    happening.save()
    return happening


def show_events():
    return Event.all()


def add_gift_to_event(event, gift):
    event.gifts.append(gift._id)
    event.save()
