from src.user.data.model import UserModel

class UserData():
    @staticmethod
    def get(email):
        user = UserModel.objects(email=email).first()
        print(user)    
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

    



        
        
        