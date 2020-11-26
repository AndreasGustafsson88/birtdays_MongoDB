from pymongo import MongoClient
from Data.db.db_settings import *


client = MongoClient(f"mongodb://{DB_USER}:{USER_PASSWORD}@{DB_HOST}:{DB_PORT}")
db = client.birthdays


class ResultList:

    def __init__(self, data):
        self.data = data

    def exists(self):
        return len(self.data) > 0


class Document(dict):
    collection = None

    def __init__(self, data):
        super().__init__()
        if "_id" not in data:
            self._id = None
        self.__dict__.update(data)

    def __repr__(self):
        return "\n".join(f"{k} = {v}" for k, v in self.__dict__.items())

    def save(self):
        if not self._id:
            del(self.__dict__["_id"])
        return self.collection.insert_one(self.__dict__)

    @classmethod
    def find(cls, **kwargs):
        return ResultList([cls(item) for item in cls.collection.find(kwargs)])
