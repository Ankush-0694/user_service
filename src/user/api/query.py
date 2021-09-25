import json
from graphene import ObjectType, String, Schema, Field,List, ID
from src.user.logic.logic import  AuthLogic
from src.user.logic.logic import UserLogic
from src.user.api.Fields import UserField
from src.utils.JWTDecorator import check_token


class UserQuery(ObjectType):
    get_user_by_email = Field(UserField, email=String()) 
    def resolve_get_user_by_email(self,  _info , email):
         return UserLogic.get_user_by_email(email)

    get_all_users_by_role = List(UserField, role=String())
    def resolve_get_all_users_by_role(self, _info, role):
        return UserLogic.get_all_users_by_role(role)
        



class AuthQuery(ObjectType):
    get_me = Field(UserField) 
    def resolve_get_me(self,  _info):
        auth_header = _info.context.headers.get("User") 

        check_token(auth_header)

        
        user_dict = json.loads(auth_header)
        print(user_dict)
        userId = user_dict["public_id"]     
        return AuthLogic.get(userId)  