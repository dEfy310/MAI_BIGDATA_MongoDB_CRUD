from django.db import models
from pymongo import MongoClient
from django.conf import settings


client = MongoClient('localhost', 27017)
db = client['musin36']

class ClassArticles:
    collection = db["articles"]

    @staticmethod
    def create(Description, Info, Name):
        return ClassArticles.collection.insert_one({"Description": Description,"Info": Info,"Name": Name})

    @staticmethod
    def readAll():
        return ClassArticles.collection.find()

    @staticmethod
    def readByName(Name):
        return ClassArticles.collection.find_one({"Name": Name})

    @staticmethod
    def update(Description, Info, Name):
        return ClassArticles.collection.update_one({"$set": {"Description": Description,"Info": Info,"Name": Name}})

    @staticmethod
    def deleteByName(Name):
        ClassArticles.collection.delete_one({"Name": Name})