from src.user.data.model import UserModel

class VendorData():
    @staticmethod
    def get_all_vendor():
        users = UserModel.objects(role="vendor")
        return users


    @staticmethod
    def create(first_name, last_name, email, password, role):
        vendor = UserModel(
            first_name=first_name, 
            last_name =last_name, 
            email = email, 
            password = password,
            role = role
        )
        return vendor.save()

    @staticmethod    
    def update(first_name, last_name, email, password, role):
        vendor = UserModel.objects(email=email).first()
        vendor.update(
            set__first_name = first_name , 
            set__last_name=last_name,
            set__role=role
        )
        vendor.reload()
        # print(vendor_user.first_name)
        return vendor
        
    @staticmethod
    def delete(email):    
        vendor = UserModel.objects(email=email).first()
        vendor.delete()
        print(vendor)
        return vendor
        