from flask import app
from mongoengine.errors import ValidationError
from src.admin.data.data import AdminData
# from flask import current_app 
from Constants.constants import *
import jwt


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

        


   
        
        



        