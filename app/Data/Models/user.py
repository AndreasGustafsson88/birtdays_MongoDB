from Data.db import Document, db
from datetime import datetime


class User(Document):
    collection = db.user

    def __init__(self, data):
        super().__init__(data)
        if not isinstance(self.__dict__["dob"], datetime):
            self.dob = datetime.strptime(self.__dict__["dob"], "%Y-%m-%d")


andreas = User({
    "first_name": "Andreas",
    "last_name": "Gustafsson",
    "dob": "1988-04-01",
    "people": []
})

