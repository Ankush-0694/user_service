from graphene.types.scalars import Boolean
from graphene import ObjectType, Mutation, String, Field
from mongoengine.fields import StringField
from src.user.api.Fields import UserField
from bson.objectid import ObjectId
from src.user.logic.logic import UserLogic, VendorLogic





class CreateUser(Mutation):
    user = Field(UserField)
    ok=Boolean();
    class Arguments:
        first_name = String()
        last_name = String()
        email = String()
        password = String()
        role = String()
        
    
    def mutate(self, _info, first_name, last_name, email, password, role):
        ok=True
        created_user =  UserLogic.create(first_name, last_name, email, password,role)
        return CreateUser(user=created_user, ok=ok) 

class UpdateUser(Mutation):
    user  = Field(UserField)
    ok=Boolean()
    class Arguments:
        first_name = String()
        last_name = String()
        email = String()
        role = String()
       
    def mutate(self, _info, first_name, last_name, email, role):     
        print(_info.context.headers.get("User")) 
        ok=True
        updated_user = UserLogic.update(first_name, last_name , email ,role  )
        return UpdateUser(user=updated_user, ok=ok)


class DeleteUser(Mutation):
    user = Field(UserField)
    ok=Boolean()
    class Arguments:  
        email = String()
    def mutate(self, _info, email):
        ok=True
        deleted_user = UserLogic.delete( email)
        return DeleteUser(user=deleted_user, ok=ok)



# # https://www.apollographql.com/blog/backend/auth/setting-up-authentication-and-authorization-apollo-federation/
# # youtube.com/watch?v=8OH4WieIKz4

# this will be added as a user login

class UserLogin(Mutation):
    token = String()
    ok=Boolean()
    class Arguments:
        email = String()
        password = String()
        role = String()
    def mutate(self, _info, email, password, role):
        # print(_info.context)
        ok = True
        generated_token = UserLogic.user_login(email, password, role)
        return UserLogin(token=generated_token,ok=ok)



class UserMutations(ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()
    user_login = UserLogin.Field()




""" 
Vendor will be created by admin , on creation
a email will be sent to the vendor then further action
"""
class CreateVendor(Mutation):
    vendor = Field(UserField)
    ok=Boolean()
    class Arguments:
        email = String()
        role = String()
        
    
    def mutate(self, _info,  email,role):
        ok=True
        created_vendor =  VendorLogic.create(email, role)
        return CreateVendor(vendor=created_vendor, ok=ok)

class GeneratePassword(Mutation):
    success_msg = String()
    ok=Boolean()
    class Arguments:
        password = String()
        verify_token = String()
        
    
    def mutate(self, _info,  password,verify_token):
        ok=True
        created_vendor =  VendorLogic.generate_password(password, verify_token)
        return GeneratePassword(success_msg="Password Generate Successfully", ok=ok)



class VendorMutation(ObjectType):
    create_vendor = CreateVendor.Field()
    generate_password = GeneratePassword.Field()

