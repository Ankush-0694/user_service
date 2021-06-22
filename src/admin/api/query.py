from graphene import ObjectType, String, Schema, Field,List, ID
from src.user.api.Fields import UserField
from src.admin.logic.logic import AdminLogic



class AdminQuery(ObjectType):
    get_all_admin = List(UserField, role=String()) 
    def resolve_get_all_admin(self,  _info , ):
        return AdminLogic.get_all_admin()