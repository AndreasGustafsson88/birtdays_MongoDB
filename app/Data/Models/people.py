from Data.db import Document, db
from datetime import datetime


class People(Document):
    collection = db.people

    def __init__(self, data):
        super().__init__(data)
        if "dob" in self.__dict__:
            self.dob = datetime.strptime(self.__dict__["dob"], "%Y-%m-%d")

    @classmethod
    def insert_all(cls, data):
        for entry in data:
            cls(entry).save()

    @classmethod
    def find_all(cls):
        return [people for people in cls.collection.find({})]
