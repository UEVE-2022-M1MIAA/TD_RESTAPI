from pymongo import MongoClient


def database():
    client = MongoClient(host="mongodb")
    db = client.warehouse
    return db
