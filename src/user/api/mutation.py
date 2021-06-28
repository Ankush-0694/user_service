from graphene.types.scalars import Boolean
from graphene import ObjectType, Mutation, String, Field
from src.user.api.Fields import UserField
from bson.objectid import ObjectId
from src.user.logic.logic import VendorLogic
from src.user.logic.logic import AdminLogic
from src.user.logic.logic import UserLogic


class CreateUser(Mutation):
    user = Field(UserField)
    ok=Boolean();
    class Arguments:
        first_name = String()
        last_name = String()
        email = String()
        password = String()
        role=String(default_value="user")
    
    def mutate(self, _info, first_name, last_name, email, password, role):
        ok=True
        created_user =  UserLogic.create(first_name, last_name, email, password,role)
        return CreateUser(user=created_user, ok=ok) 


class UserMutations(ObjectType):
    create_user = CreateUser.Field()




def login_middleware(header_user) :
    if header_user == 'null':
        raise PermissionError("You are not logged In")
    else:
        pass

# def check_role_admin(header_user):
#     userId = json.loads(header_user)
#     userObjectID = ObjectId(userId["public_id"])
#     print(userObjectID)
#     role = AdminData.check_admin(userObjectID)
#     if role!="admin":
#         raise PermissionError("You Are not an admin")





class CreateAdmin(Mutation):
    admin = Field(UserField)
    ok=Boolean()
    class Arguments:
        first_name = String()
        last_name = String()
        email = String()
        password = String()
        role=String(default_value="admin")
    def mutate(self, _info, first_name, last_name, email, password, role):
        ok=True
        created_admin = AdminLogic.create_admin(
            first_name, last_name , email, password ,role 
        )
        return CreateAdmin(admin=created_admin, ok=ok) 
    
 

# for updating password , we need to write different Mutation 
class UpdateAdmin(Mutation):
    admin = Field(UserField)
    ok=Boolean()
    class Arguments:
        first_name = String()
        last_name = String()
        email = String()
        password = String()
        role=String(default_value="admin")
    def mutate(self, _info, first_name, last_name, email, password, role):     
        print(_info.context.headers.get("User")) # fetching request.header but we need to add to the schema context (_info.context.user)

        # if _info.context.headers.get("User") == "null":
        #     raise PermissionError("You are not logged In")
        login_middleware(_info.context.headers.get("User"))


        ok=True
        updated_admin = AdminLogic.update_admin(first_name, last_name , email, password ,role  )
        return UpdateAdmin(admin=updated_admin, ok=ok) 



class DeleteAdmin(Mutation):
    admin = Field(UserField)
    ok=Boolean()
    class Arguments:  
        email = String()
    def mutate(self, _info, email):
        ok=True
        deleted_admin = AdminLogic.delete_admin( email)
        return DeleteAdmin(admin=deleted_admin, ok=ok)




class AdminLogin(Mutation):
    token = String()
    ok=Boolean()
    class Arguments:
        email = String()
        password = String()
    def mutate(self, _info, email, password):
        # print(_info.context)
        ok = True
        generated_token = AdminLogic.admin_login(email, password)
        return AdminLogin(token=generated_token,ok=ok)




class AdminMutations(ObjectType):
    create_admin = CreateAdmin.Field()
    update_admin = UpdateAdmin.Field()
    delete_admin = DeleteAdmin.Field()
    admin_login  =  AdminLogin.Field()

# https://www.apollographql.com/blog/backend/auth/setting-up-authentication-and-authorization-apollo-federation/
# youtube.com/watch?v=8OH4WieIKz4

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
