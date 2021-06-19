from src.user.data.data import UserData

class UserLogic():
    @staticmethod
    def get(email): 
        users = UserData.get(email)
        for user in users:
            print(user)
            return user

    @staticmethod
    def create(first_name, last_name, email, password, role):
        user =  UserData.create(first_name, last_name, email, password, role)

        # need to edit user object before sending to the client or maybe not
        print(user.role.value)
        user.role = user.role.value
        
        return user

         

