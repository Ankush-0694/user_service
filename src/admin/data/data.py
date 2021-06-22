from src.user.data.model import UserModel

class AdminData():
    @staticmethod
    def get_all_admin():
        users = UserModel.objects(role="admin")
        return users


    @staticmethod
    def create_admin(first_name, last_name, email, password, role):
        admin_user = UserModel(
            first_name=first_name, 
            last_name =last_name, 
            email = email, 
            password = password,
            role = role
        )
        return admin_user.save()

    @staticmethod    
    def update_admin(first_name, last_name, email, password, role):
        admin_user = UserModel.objects(email=email).first()
        admin_user.update(
            set__first_name = first_name , 
            set__last_name=last_name,
            set__role=role
        )
        admin_user.reload()
        # print(admin_user.first_name)
        return admin_user
        
    @staticmethod
    def delete_admin(email):    
        admin_user = UserModel.objects(email=email).first()
        admin_user.delete()
        print(admin_user)
        return admin_user
        