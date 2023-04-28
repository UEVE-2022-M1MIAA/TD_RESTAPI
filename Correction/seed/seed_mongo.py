"""Module used to fill a mongo database with defined data.
"""

from pymongo import MongoClient


class MongoSeeder:
    def __init__(self):
        host = "mongodb"
        client = MongoClient(host=f"{host}")
        self.__db = client.warehouse

    @property
    def db(self):
        return self.__db

    def seed(self):
        """Seeds the database."""

        # Clearing collection
        self.__db.warehouse.delete_many({})

        # Insert valid and invalid data
        warehouse = []

        # Valid data
        valid_immat = "AB1001S 01FE"
        egg = {"immat": valid_immat, "color": "brown", "breeding": "Cocotte"}
        warehouse.append(egg)

        # Invalid data
        invalid_immat = "BB1000S 01FE"
        egg = {"immat": invalid_immat, "color": "white", "breeding": "Cocotte"}
        warehouse.append(egg)

        self.__db.warehouse.insert_many(warehouse)

        cursor = self.__db.warehouse.find()
        for egg in cursor:
            print(egg)


if __name__ == "__main__":
    print("Filling DB with eggs")
    MongoSeeder().seed()
    print("Done")
