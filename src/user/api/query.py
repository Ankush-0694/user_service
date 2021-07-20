import json
from graphene import ObjectType, String, Schema, Field,List, ID
from src.user.logic.logic import  AuthLogic
from src.user.api.Fields import UserField
from src.user.logic.logic import UserLogic
# from src.user.logic.logic import VendorLogic

class UserQuery(ObjectType):
    get_user_by_email = Field(UserField, email=String()) 
    def resolve_get_user_by_email(self,  _info , email):
         return UserLogic.get_user_by_email(email)

    get_all_users_by_role = List(UserField, role=String())
    def resolve_get_all_users_by_role(self, _info, role):
        return UserLogic.get_all_users_by_role(role)
        

# class AdminQuery(ObjectType):
#     get_all_admin = List(UserField, role=String()) 
#     def resolve_get_all_admin(self,  _info , ):
#         return AdminLogic.get_all_admin()

# class VendorQuery(ObjectType):
#     get_all_vendor = List(UserField, role=String()) 
#     def resolve_get_all_vendor(self,  _info , ):
#         return VendorLogic.get_all_vendor()

class AuthQuery(ObjectType):
    get_me = Field(UserField) 
    def resolve_get_me(self,  _info):
        auth_header = _info.context.headers.get("User") 
        print(auth_header)
        if auth_header == "null":
            raise PermissionError("You need to pass token as a header")

        email_id_dict = json.loads(auth_header)
        email = email_id_dict["public_id"]     
        return AuthLogic.get(email)  