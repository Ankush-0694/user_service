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
    



        
# class AdminData():
#     @staticmethod
#     def get_all_admin():
#         admins = UserModel.objects(role="admin")
#         return admins

#     @staticmethod
#     def check_admin(id):
#         data = UserModel.objects(id = id).first()
#         print(data.role)
#         return data.role
        
        

#     @staticmethod
#     def create_admin(first_name, last_name, email, password, role):

#         #checking, If there is any admin with the given email id or not
#         admin = UserModel.objects(email=email).first()
#         if admin:
#             raise ValidationError("Email already exist")
        
       

#         admin = UserModel(
#             first_name=first_name, 
#             last_name =last_name, 
#             email = email, 
#             password = password,
#             role = role
#         )
#         return admin.save()

#     @staticmethod    
#     def update_admin(first_name, last_name, email, password, role):
#         admin = UserModel.objects(email=email).first()
#         admin.update(
#             set__first_name = first_name , 
#             set__last_name=last_name,
#             set__role=role
#         )
#         admin.reload()
#         # print(admin.first_name)
#         return admin
        
#     @staticmethod
#     def delete_admin(email):    
#         admin = UserModel.objects(email=email).first()
#         admin.delete()
#         print(admin)
#         return admin


#     @staticmethod
#     def admin_login(email, password):
#         user = UserModel.objects(email=email).first()
#         if not user:
#             raise ValidationError('User Not Found')
            
#         if user.password != password:
#             raise ValidationError("Password Not Matched")
#         return user

        
# class VendorData():
#     @staticmethod
#     def get_all_vendor():
#         users = UserModel.objects(role="vendor")
#         return users


#     @staticmethod
#     def create(first_name, last_name, email, password, role):
#         vendor = UserModel(
#             first_name=first_name, 
#             last_name =last_name, 
#             email = email, 
#             password = password,
#             role = role
#         )
#         return vendor.save()

#     @staticmethod    
#     def update(first_name, last_name, email, password, role):
#         vendor = UserModel.objects(email=email).first()
#         vendor.update(
#             set__first_name = first_name , 
#             set__last_name=last_name,
#             set__role=role
#         )
#         vendor.reload()
#         # print(vendor_user.first_name)
#         return vendor
        
#     @staticmethod
#     def delete(email):    
#         vendor = UserModel.objects(email=email).first()
#         vendor.delete()
#         print(vendor)
#         return vendor


class AuthData():
    @staticmethod
    def get(email):
        me = UserModel.objects(email=email).first()
        return me