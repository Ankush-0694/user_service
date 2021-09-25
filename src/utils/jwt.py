import jwt
from datetime import datetime, timedelta

from mongoengine import errors
from Constants.constants import SECRET_KEY

# helper function for generating jwt
def generate_token(userId,  role):
        token = jwt.encode({
            'public_id': userId,
            'role': role
            
        }, SECRET_KEY, algorithm="HS256")
        token = token.decode('UTF-8')
        return token


def generate_token_for_mail(public_id):

        token = jwt.encode({
            'public_id': public_id,
            'exp' : datetime.utcnow() + timedelta(hours = 24)
        }, SECRET_KEY, algorithm="HS256")
        token = token.decode('UTF-8')

        return token

def decode_token(token):
   
    payload = jwt.decode(
        token, SECRET_KEY , algorithms="HS256"
    )
    return payload
   

    

    


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



# print(_info.context.headers.get("User"))  # for getting header data