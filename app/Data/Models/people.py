from Data.db import Document, db
from datetime import datetime


class People(Document):
    collection = db.people

    def __init__(self, data):
        super().__init__(data)
        if not isinstance(self.__dict__["dob"], datetime):
            self.dob = datetime.strptime(self.__dict__["dob"], "%Y-%m-%d")
