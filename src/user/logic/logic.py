from src.user.data.data import UserData

class UserLogic():
    @staticmethod
    def get(email): 
        users = UserData.get(email)
        for user in users:
            print(user)
            return user


         
