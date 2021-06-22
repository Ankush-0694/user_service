from graphene import ObjectType, String, ID

class UserField(ObjectType):
    id = ID()
    first_name = String()
    last_name = String()
    email = String()
    role = String()
    

