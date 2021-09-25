from Constants.constants import CLIENT_URL
import json
from mongoengine import errors
from src.user.data.data import  AuthData, VendorData
from src.user.data.data import  UserData
from src.utils.jwt import decode_token, generate_token, generate_token_for_mail
from src.utils.emailer import send_email
from bson import json_util
from flask_mail import  Message






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
    def user_login(email, password, role):
        user = UserData.user_login(email, password, role)
        role = user["role"]

        # getting object id created from the MongoDB database
        userId = user["id"]   

        # changin object Id to json using some packages
        userId = json.loads(json_util.dumps(userId))  

        # storing user id from dictionary create from previous step
        userId = userId['$oid']
      
        

        """ Generating token  """
        token = generate_token(userId,  role)
        print(token)
        return token
        

class VendorLogic():
    def create(email, role):

        verificationToken = generate_token_for_mail(email)

        vendor = VendorData.create(email,role, verificationToken)

        link_for_password_generation = "%s/vendor/generatePassword/" % CLIENT_URL + str(verificationToken)

        # mail data to send
        msgData = Message('You are authorized to become a vendor' ,  recipients=[email])
        msgData.body = 'You can generate password and enter your details by clicking on below link-'
        msgData.html = '<p>link - %s </p>' % link_for_password_generation

        try:
            send_email(msgData)
        except :
            raise Exception("Error in Sending Emails")
        
        return vendor

    def generate_password(password, verify_token):

        # check token is valid or not
        try:
            decoded_token = decode_token(verify_token)
        except:
            raise Exception("Incorect link or it is expired.")

        vendor_email = decoded_token["public_id"]

        # need to check token is in database or not (generate a password only one time with one link)
        VendorData.check_for_verify_token(vendor_email)
       
        updated_vendor = VendorData.generate_password(password, vendor_email)

        return updated_vendor





          

class AuthLogic():
    @staticmethod
    def get(userId):
        me = AuthData.get(userId)
        return me