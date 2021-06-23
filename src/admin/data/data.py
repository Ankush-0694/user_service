from mongoengine.errors import ValidationError
from src.user.data.model import UserModel



class AdminData():
    @staticmethod
    def get_all_admin():
        users = UserModel.objects(role="admin")
        return users


    @staticmethod
    def create_admin(first_name, last_name, email, password, role):

        #checking, If there is any admin with the given email id or not

        admin_user = UserModel.objects(email=email).first()
        if admin_user:
            raise ValidationError("Email already exist")
        
        # manually giving validation for every field
        if last_name == "":
            raise ValidationError('value can not be empty')

        admin_user = UserModel(
            first_name=first_name, 
            last_name =last_name, 
            email = email, 
            password = password,
            role = role
        )
        return admin_user.save()

    @staticmethod    
    def update_admin(first_name, last_name, email, password, role):
        admin_user = UserModel.objects(email=email).first()
        admin_user.update(
            set__first_name = first_name , 
            set__last_name=last_name,
            set__role=role
        )
        admin_user.reload()
        # print(admin_user.first_name)
        return admin_user
        
    @staticmethod
    def delete_admin(email):    
        admin_user = UserModel.objects(email=email).first()
        admin_user.delete()
        print(admin_user)
        return admin_user


    @staticmethod
    def admin_login(email, password):
        user = UserModel.objects(email=email).first()
        if not user:
            raise ValidationError('User Not Found')
            
        if user.password != password:
            raise ValidationError("Password Not Matched")
        return user

        