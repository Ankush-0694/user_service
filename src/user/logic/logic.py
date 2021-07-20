from src.user.data.data import  AuthData
from src.user.data.data import  UserData
from src.utils.jwt import generate_token





class UserLogic():
    @staticmethod
    def get_user_by_email(email):  
        user = UserData.get_user_by_email(email)
        return user
    
    @staticmethod
    def get_all_users_by_role(role):  
        user = UserData.get_all_users_by_role(role)
        return user

    @staticmethod
    def create(first_name, last_name, email, password, role):
        user =  UserData.create(first_name, last_name, email, password, role)
        return user

    @staticmethod
    def update(first_name, last_name, email, password, role):
        user = UserData.update(first_name, last_name, email, password, role)
        return user

    @staticmethod
    def delete(email):
        user = UserData.delete(email)
        return user
   
         

# class AdminLogic():
#     @staticmethod
#     def get_all_admin():
#         all_admins = AdminData.get_all_admin()
#         return all_admins

    

#     @staticmethod
#     def create_admin(first_name, last_name, email, password, role):
#         admin = AdminData.create_admin(first_name, last_name, email, password, role)
#         return admin

#     @staticmethod
#     def update_admin(first_name, last_name, email, password, role):
#         admin = AdminData.update_admin(first_name, last_name, email, password, role)
#         return admin

#     @staticmethod
#     def delete_admin(email):
#         admin = AdminData.delete_admin(email)
#         return admin
    
    
#     @staticmethod
#     def admin_login(email, password):
#         admin = AdminData.admin_login(email, password)
#         # print(type(str(user.id)))
#         # token = generate_token(str(admin.id))
#         token = generate_token(email)
#         print(token)
#         return token;


# class VendorLogic():
#     @staticmethod
#     def get_all_vendor():
#         all_vendors = VendorData.get_all_vendor()
#         return all_vendors


#     @staticmethod
#     def create(first_name, last_name, email, password, role):
#         vendor = VendorData.create(first_name, last_name, email, password, role)
#         return vendor

#     @staticmethod
#     def update(first_name, last_name, email, password, role):
#         vendor = VendorData.update(first_name, last_name, email, password, role)
#         return vendor

#     @staticmethod
#     def delete(email):
#         vendor = VendorData.delete(email)
#         return vendor


class AuthLogic():
    @staticmethod
    def get(email):
        me = AuthData.get(email)
        return me