import pymongo
import os
from urllib.parse import quote_plus


import certifi
ca = certifi.where()

class MongodbOperation:

    def __init__(self) -> None:
        username = "maheshjadhav7979"
        password = "Mahesh@15698"
        # MONGO_DB_URL = "mongodb://{}:{}@your_mongodb_host:your_mongodb_port/your_database".format(quote_plus(username), quote_plus(password))

        # Now you can use MONGO_DB_URL in your MongoClient initialization.

        MONGO_DB_URL = "mongodb+srv://{}:{}@cluster0.odlnycj.mongodb.net/?retryWrites=true&w=majority".format(quote_plus(username), quote_plus(password))
        # MONGO_DB_URL ="mongodb+srv://maheshjadhav7979:Mahesh@15698@cluster0.odlnycj.mongodb.net/"
        self.client = pymongo.MongoClient(MONGO_DB_URL,tlsCAFile=ca)
        self.db_name="MaheshDB"

    def insert_many(self,collection_name,records:list):
        self.client[self.db_name][collection_name].insert_many(records)

    def insert(self,collection_name,record):
        self.client[self.db_name][collection_name].insert_one(record)
        
