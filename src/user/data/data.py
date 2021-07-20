from src.user.data.model import UserModel
from mongoengine.errors import ValidationError


class UserData(): 
    @staticmethod
    def get_user_by_email(email):
        user = UserModel.objects(email=email).first()     
        return user
    
    @staticmethod
    def get_all_users_by_role(role):
        user = UserModel.objects(role=role)
        return user

    @staticmethod
    def create(first_name, last_name, email, password, role):
        user = UserModel(
            first_name=first_name, 
            last_name =last_name, 
            email = email, 
            password = password,
            role = role
        )
        return user.save()

    @staticmethod
    def update(first_name, last_name, email, password, role):
        user  = UserModel.objects(email=email).first()
        user.update(
            set__first_name = first_name , 
            set__last_name=last_name,
            set__role=role
        )
        user.reload()
        return user


    @staticmethod
    def delete(email):    
        user = UserModel.objects(email=email).first()
        user.delete()
        print(user)
        return user
    



class AuthData():
    @staticmethod
    def get(email):
        me = UserModel.objects(email=email).first()
        return me