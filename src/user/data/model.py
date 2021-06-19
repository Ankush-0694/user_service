# from mongoengine import *
from mongoengine.document import Document
from mongoengine.fields import EnumField, StringField
from enum import Enum

class Role(Enum):
    admin = "admin"
    user = "user"
    vendor = "vendor"




class User(Document):
    first_name = StringField()
    last_name = StringField()
    email= StringField()
    password = StringField()
    role = EnumField(Role)

# print(User)
