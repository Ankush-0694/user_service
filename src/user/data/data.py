from src.user.data.model import User

class UserData():
    @staticmethod
    def get(email):
        user = User.objects(email=email)
        return user
