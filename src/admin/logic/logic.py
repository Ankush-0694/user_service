from src.admin.data.data import AdminData

class AdminLogic():
    @staticmethod
    def get_all_admin():
        all_admins = AdminData.get_all_admin()
        return all_admins


    @staticmethod
    def create_admin(first_name, last_name, email, password, role):
        admin_user = AdminData.create_admin(first_name, last_name, email, password, role)
        return admin_user

    @staticmethod
    def update_admin(first_name, last_name, email, password, role):
        admin_user = AdminData.update_admin(first_name, last_name, email, password, role)
        return admin_user

    @staticmethod
    def delete_admin(email):
        admin_user = AdminData.delete_admin(email)
        return admin_user