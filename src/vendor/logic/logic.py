from src.vendor.data.data import VendorData

class VendorLogic():
    @staticmethod
    def get_all_vendor():
        all_vendors = VendorData.get_all_vendor()
        return all_vendors


    @staticmethod
    def create(first_name, last_name, email, password, role):
        vendor = VendorData.create(first_name, last_name, email, password, role)
        return vendor

    @staticmethod
    def update(first_name, last_name, email, password, role):
        vendor = VendorData.update(first_name, last_name, email, password, role)
        return vendor

    @staticmethod
    def delete(email):
        vendor = VendorData.delete(email)
        return vendor