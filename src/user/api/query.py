from graphene import ObjectType, String, Schema, Field,List, ID
from src.user.api.Fields import UserField
from src.user.logic.logic import UserLogic



class UserQuery(ObjectType):
    get_user = Field(UserField, email=String()) 
    def resolve_get_user(self,  _info , email):
        return UserLogic.get(email)
        


        