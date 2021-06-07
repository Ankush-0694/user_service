from graphene import ObjectType, String, Schema, Field,List, ID


#GraphQL Schema
class User(ObjectType):
    first_name = String()
    last_name = String()
    email = String()
    password = String()
    

