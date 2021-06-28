from mongoengine.errors import ValidationError
from src.user.data.model import UserModel



class AdminData():
    @staticmethod
    def get_all_admin():
        admins = UserModel.objects(role="admin")
        return admins

    @staticmethod
    def check_admin(id):
        data = UserModel.objects(id = id).first()
        print(data.role)
        return data.role
        
        

    @staticmethod
    def create_admin(first_name, last_name, email, password, role):

        #checking, If there is any admin with the given email id or not
        admin = UserModel.objects(email=email).first()
        if admin:
            raise ValidationError("Email already exist")
        
       

        admin = UserModel(
            first_name=first_name, 
            last_name =last_name, 
            email = email, 
            password = password,
            role = role
        )
        return admin.save()

    @staticmethod    
    def update_admin(first_name, last_name, email, password, role):
        admin = UserModel.objects(email=email).first()
        admin.update(
            set__first_name = first_name , 
            set__last_name=last_name,
            set__role=role
        )
        admin.reload()
        # print(admin.first_name)
        return admin
        
    @staticmethod
    def delete_admin(email):    
        admin = UserModel.objects(email=email).first()
        admin.delete()
        print(admin)
        return admin


    @staticmethod
    def admin_login(email, password):
        user = UserModel.objects(email=email).first()
        if not user:
            raise ValidationError('User Not Found')
            
        if user.password != password:
            raise ValidationError("Password Not Matched")
        return user

        