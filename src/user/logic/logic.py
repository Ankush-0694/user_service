from src.user.data.data import  AuthData, VendorData
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
    
    @staticmethod
    def user_login(email, password):
        user = UserData.user_login(email, password)
        token = generate_token(email)
        print(token)
        return token;
        



class VendorLogic():
    def create(email, role):
        vendor = VendorData.create(email,role)
        return vendor


          

class AuthLogic():
    @staticmethod
    def get(email):
        me = AuthData.get(email)
        return me