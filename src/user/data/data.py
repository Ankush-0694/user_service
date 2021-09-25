from mongoengine import errors
from mongoengine.queryset.base import NULLIFY
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

        # we only check using email (because with same email two roles can not be there)
        
        if UserModel.objects(email=email).first() :
            return ValidationError(message="User Already Exists")
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
    
    @staticmethod
    def user_login(email, password, role):

        # we need to match both role and email 
        #if we match only email then other user can login from another login page

        

        user = UserModel.objects(email=email).first()
        if not user or  user.password != password:
            raise ValidationError('You have entered an invalid username or password')

        if user.role != role:
            raise ValidationError("You have already an account with another role")

            
        return user


class VendorData():
    def create(email , role , verificationToken):
        is_vendor_exist = UserModel.objects(email=email).first()

        if is_vendor_exist:
            raise ValidationError('User Already Exists')

        user = UserModel(           
            email = email,             
            role = role,
            verify_token = verificationToken
        )
        return user.save()

    def generate_password(password, email):
        is_user_exist = UserModel.objects(email=email).first()

        if not is_user_exist:
            raise ValidationError("User does not exist")

        update_user = UserModel.objects(email=email).update_one(verify_token="",password=password)
        
        update_user.reload()
        

        return update_user

    def check_for_verify_token(email):
        user = UserModel.objects(email=email).first()

        if not user.verify_token :
            raise Exception("Incorect link or it is expired.")

        return user
        

            
        
    





class AuthData():
    @staticmethod
    def get(userId):
        me = UserModel.objects(id=userId).first()
        if not me:
            raise ValidationError("User not found")
        return me