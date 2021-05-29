from graphene import ObjectType, String, Schema, Field,List, ID


#GraphQL Schema
class User(ObjectType):
    firstName = String()
    lastName = String()
    # email = String()
    # password = String()
    

