from graphene import ObjectType, String, Schema, Field,List, ID
from src.user.logic.logic import AdminLogic
from src.user.api.Fields import UserField
from src.user.logic.logic import UserLogic
from src.user.logic.logic import VendorLogic

class UserQuery(ObjectType):
    get_user = Field(UserField, email=String()) 
    def resolve_get_user(self,  _info , email):
        return UserLogic.get(email)
        

class AdminQuery(ObjectType):
    get_all_admin = List(UserField, role=String()) 
    def resolve_get_all_admin(self,  _info , ):
        return AdminLogic.get_all_admin()

class VendorQuery(ObjectType):
    get_all_vendor = List(UserField, role=String()) 
    def resolve_get_all_vendor(self,  _info , ):
        return VendorLogic.get_all_vendor()