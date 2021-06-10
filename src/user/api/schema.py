from graphene import ObjectType, String, Schema, Field,List, ID
from graphene_federation import provides

#GraphQL Schema

class User(ObjectType):
    first_name = String()
    last_name = String()
    email = String()
    password = String()
    

