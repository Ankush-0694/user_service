from src.user.data.data import  UserData

class UserLogic():
    @staticmethod
    def get(email):  
        user = UserData.get(email)
        return user

    @staticmethod
    def create(first_name, last_name, email, password, role):
        user =  UserData.create(first_name, last_name, email, password, role)
        return user
   
         




