# from mongoengine import *
from mongoengine.document import Document
from mongoengine.fields import StringField



class User(Document):
    first_name = StringField()
    last_name = StringField()
    email= StringField()
    password = StringField()
