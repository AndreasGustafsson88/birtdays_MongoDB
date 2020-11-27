from Data.db import Document, db


class Event(Document):
    collection = db.events


events = Event.all()

for event in events:
    print(event)
    