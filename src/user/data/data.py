from src.user.data.model import User

class UserData():
    @staticmethod
    def get(email):
        user = User.objects(email=email)
        return user

    @staticmethod
    def create(first_name, last_name, email, password):
        # print(first_name)
        user = User(
            first_name=first_name, 
            last_name =last_name, 
            email = email, 
            password = password
        )
        # print(user)
        return user.save()
        