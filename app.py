import re
from flask import Flask, render_template, request, json, make_response, jsonify
from flask_cors import CORS
# from werkzeug.security import generate_password_hash, check_password_hash
from flask_pymongo import PyMongo
from flask_jwt import jwt
from datetime import datetime, timedelta
# from flask_bcrypt import Bcrypt
from bson import ObjectId
from functools import wraps



app = Flask(__name__)
CORS(app)

# bcrypt = Bcrypt(app)



app.config['SECRET_KEY'] = "randomsecretkey"
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)




#need a decorator which we will run every time a protected route will be visited 
# Decorator is like a middleware
# this decorator which check that , there is a token passed in the header or not
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401

        try: 
            data = jwt.decode(token, app.config['SECRET_KEY'])
            publicId = data["public_id"]
            publicId = publicId.replace('"', '')  # removing extra quotes from the _id
            publicId = ObjectId(publicId)
           
            current_user = mongo.db.users.find_one({"_id": publicId })
            print(current_user)# why it is giving none 
            
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401
        
        
        return f(current_user, *args, **kwargs)

    return decorated

# test route
@app.route('/')
def hello_world():
    return 'Hello, World!'


#test protected route
@app.route('/admin')
@token_required
def protectedRoute(current_user):
    # print(current_user)
    return "Welcome to protected route"



#signup route
@app.route('/auth/signup', methods=["POST"])
def Signup():
     
    if request.method == "POST":
        
        request_data = json.loads(request.data)
        password = request_data["password"]
        # hashed_password = generate_password_hash(request_data['password'], method='sha256')
        # hashed_password = bcrypt.generate_password_hash(request_data['password']).decode('utf8')
        newUser = {
            'firstName': request_data['firstName'],
            'lastName': request_data['lastName'], 
            'email': request_data['email'], 
            'password': password 
         }


         # find the user from database , if user found then response already exist  else
         # we will do the further work
        user = mongo.db.users.find_one({'email': request_data['email']})
      

        if user:
            return make_response(
                'Could not verify',
                409,
                {'WWW-Authenticate' : 'Basic realm ="User already exist !!"'}
            )

         
   
        user_collections = mongo.db.users
        user_collections.insert(newUser)

        return make_response('Successfully registered.', 201)

 
#login route
@app.route('/auth/login', methods=["POST"])
def login():
     
    if request.method == "POST":
       
        request_data = json.loads(request.data)
        # print(request_data)


        #finding the user from database
        user = mongo.db.users.find_one({"email": request_data["email"] })
        # print(user)
       

       #check user is exist in database or not
        if not user:
            return make_response(
                'Could not verify',
                401,
                {'WWW-Authenticate' : 'Basic realm ="User does not exist !!"'}
            )


        # print(bcrypt.check_password_hash(user["password"], request_data["password"]))  #error occured here


        # method to change ObjectId() to string
        class JSONEncoder(json.JSONEncoder):
            def default(self, o):
                if isinstance(o, ObjectId):
                    return str(o)
                return json.JSONEncoder.default(self, o)

       

        if  (user["password"]== request_data["password"]):
            # generate the token
            token = jwt.encode({
                'public_id': JSONEncoder().encode(user["_id"]),
                'exp' : datetime.utcnow() + timedelta(minutes = 30)
            }, 
            app.config['SECRET_KEY'])
    
            return make_response(jsonify({'token' : token.decode('UTF-8')}), 201)


        return make_response(
            'Could not verify',
            403,
            {'WWW-Authenticate' : 'Basic realm ="Wrong Password !!"'}
        )


if __name__ == "__main__":
    app.run(debug=True , port = 4000)




