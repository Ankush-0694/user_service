from src.user.data.data import UserData

class UserLogic():
    @staticmethod
    def get(email):
        return UserData.get(email)
         
