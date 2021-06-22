from graphene import ObjectType, String, Schema, Field,List, ID
from src.user.api.Fields import UserField
from src.vendor.logic.logic import VendorLogic



class VendorQuery(ObjectType):
    get_all_vendor = List(UserField, role=String()) 
    def resolve_get_all_vendor(self,  _info , ):
        return VendorLogic.get_all_vendor()