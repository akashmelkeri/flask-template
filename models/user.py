from pymongo import ASCENDING, DESCENDING

class User:
    collection = None

    @classmethod
    def initialize_db(cls, db):
        cls.collection = db['users']
        cls.collection.create_index([('username', ASCENDING)], unique=True)

    @classmethod
    def create(cls, username, email, password):
        user = {
            'username': username,
            'email': email,
            'password': password,
        }
        cls.collection.insert_one(user)

    @classmethod
    def find_by_username(cls, username):
        return cls.collection.find_one({'username': username})

    @classmethod
    def find_all(cls):
        return cls.collection.find().sort('username', ASCENDING)

    @classmethod
    def delete(cls, username):
        cls.collection.delete_one({'username': username})