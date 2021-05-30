from src.user.data.data import UserData

class UserLogic():
    @staticmethod
    def get(email): 
        users = UserData.get(email)
        for user in users:
            print(user)
            return user

    @staticmethod
    def create(first_name, last_name, email, password):
        user =  UserData.create(first_name, last_name, email, password)
        # userObject = {
        #     "first_name" : user.first_name,
        #     "last_name" : user.last_name,
        #     "email" : user.email,
        #     "password" : user.password,
        # }
        
        return user

         
