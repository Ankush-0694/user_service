from src.user.data.data import AdminData
from src.user.data.data import  UserData
from Constants.constants import *
import jwt
from src.user.data.data import VendorData

class UserLogic():
    @staticmethod
    def get(email):  
        user = UserData.get(email)
        return user

    @staticmethod
    def create(first_name, last_name, email, password, role):
        user =  UserData.create(first_name, last_name, email, password, role)
        return user
   
         

    




class AdminLogic():
    @staticmethod
    def get_all_admin():
        all_admins = AdminData.get_all_admin()
        return all_admins

    

    @staticmethod
    def create_admin(first_name, last_name, email, password, role):
        admin = AdminData.create_admin(first_name, last_name, email, password, role)
        return admin

    @staticmethod
    def update_admin(first_name, last_name, email, password, role):
        admin = AdminData.update_admin(first_name, last_name, email, password, role)
        return admin

    @staticmethod
    def delete_admin(email):
        admin = AdminData.delete_admin(email)
        return admin


    # helper function for generating jwt
    @staticmethod 
    def generate_token(id):
        token = jwt.encode({
            'public_id': id,
        }, secret_key, algorithm="HS256")
        token = token.decode('UTF-8')
        return token
      
    
    @staticmethod
    def admin_login(email, password):
        admin = AdminData.admin_login(email, password)
        # print(type(str(user.id)))
        token = AdminLogic.generate_token(str(admin.id))
        print(token)
        return token;


class VendorLogic():
    @staticmethod
    def get_all_vendor():
        all_vendors = VendorData.get_all_vendor()
        return all_vendors


    @staticmethod
    def create(first_name, last_name, email, password, role):
        vendor = VendorData.create(first_name, last_name, email, password, role)
        return vendor

    @staticmethod
    def update(first_name, last_name, email, password, role):
        vendor = VendorData.update(first_name, last_name, email, password, role)
        return vendor

    @staticmethod
    def delete(email):
        vendor = VendorData.delete(email)
        return vendor