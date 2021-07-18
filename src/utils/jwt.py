import jwt
from Constants.constants import *

# helper function for generating jwt
def generate_token(email):
        token = jwt.encode({
            'public_id': email,
        }, secret_key, algorithm="HS256")
        token = token.decode('UTF-8')
        return token





# def login_middleware(header_user) :
#     if header_user == 'null':
#         raise PermissionError("You are not logged In")
#     else:
#         pass

# def check_role_admin(header_user):
#     userId = json.loads(header_user)
#     userObjectID = ObjectId(userId["public_id"])
#     print(userObjectID)
#     role = AdminData.check_admin(userObjectID)
#     if role!="admin":
#         raise PermissionError("You Are not an admin")