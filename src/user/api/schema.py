from graphene import ObjectType, String, ID

class User(ObjectType):
    id = ID()
    first_name = String()
    last_name = String()
    email = String()
    password = String()
    role = String()
    

