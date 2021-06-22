from graphene.types.scalars import Boolean
from src.vendor.logic.logic import VendorLogic
from graphene import ObjectType, Mutation, String, Field
from src.user.api.Fields import UserField



class CreateVendor(Mutation):
    vendor = Field(UserField)
    ok=Boolean()
    class Arguments:
        first_name = String()
        last_name = String()
        email = String()
        password = String()
        role=String(default_value="vendor")
    def mutate(self, _info, first_name, last_name, email, password, role):
        ok=True
        created_vendor = VendorLogic.create(first_name, last_name , email, password ,role  )
        return CreateVendor(vendor=created_vendor, ok=ok) 
    
 


class UpdateVendor(Mutation):
    vendor = Field(UserField)
    ok=Boolean()
    class Arguments:
        first_name = String()
        last_name = String()
        email = String()
        password = String()
        role=String(default_value="vendor")
    def mutate(self, _info, first_name, last_name, email, password, role):
        ok=True
        updated_vendor = VendorLogic.update(first_name, last_name , email, password ,role  )
        return UpdateVendor(vendor=updated_vendor, ok=ok) 



class DeleteVendor(Mutation):
    vendor = Field(UserField)
    ok=Boolean()
    class Arguments:  
        email = String()
    def mutate(self, _info, email):
        ok=True
        deleted_vendor = VendorLogic.delete( email  )
        return DeleteVendor(vendor=deleted_vendor, ok=ok) 

class VendorMutations(ObjectType):
    create_vendor = CreateVendor.Field()
    update_vendor = UpdateVendor.Field()
    delete_vendor = DeleteVendor.Field()
