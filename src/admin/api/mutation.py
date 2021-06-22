from graphene.types.scalars import Boolean
from src.admin.logic.logic import AdminLogic
from graphene import ObjectType, Mutation, String, Field
from src.user.api.Fields import UserField



class CreateAdmin(Mutation):
    admin_user = Field(UserField)
    ok=Boolean()
    class Arguments:
        first_name = String()
        last_name = String()
        email = String()
        password = String()
        role=String(default_value="admin")
    def mutate(self, _info, first_name, last_name, email, password, role):
        ok=True
        created_admin_user = AdminLogic.create_admin(
            first_name, last_name , email, password ,role 
        )
        return CreateAdmin(admin_user=created_admin_user, ok=ok) 
    
 


class UpdateAdmin(Mutation):
    admin_user = Field(UserField)
    ok=Boolean()
    class Arguments:
        first_name = String()
        last_name = String()
        email = String()
        password = String()
        role=String(default_value="admin")
    def mutate(self, _info, first_name, last_name, email, password, role):
        ok=True
        updated_admin_user = AdminLogic.update_admin(first_name, last_name , email, password ,role  )
        return UpdateAdmin(admin_user=updated_admin_user, ok=ok) 



class DeleteAdmin(Mutation):
    admin_user = Field(UserField)
    ok=Boolean()
    class Arguments:  
        email = String()
    def mutate(self, _info, email):
        ok=True
        deleted_admin = AdminLogic.delete_admin( email  )
        return DeleteAdmin(admin_user=deleted_admin, ok=ok) 

class AdminMutations(ObjectType):
    create_admin = CreateAdmin.Field()
    update_admin = UpdateAdmin.Field()
    delete_admin = DeleteAdmin.Field()
