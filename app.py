from flask import Flask, render_template, request, json
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash






app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = "randomsecretkey"


users = [] # user database dictionary

# test route
@app.route('/')
def hello_world():
    return 'Hello, World!'


#signup route

@app.route('/auth/signup', methods=["POST"])
def Signup():
     
    if request.method == "POST":
        request_data = json.loads(request.data)
        password = request_data["password"]
        hashed_password = generate_password_hash(request_data['password'], method='sha256')
        newUser = {'firstName': request_data['firstName'], 'lastName': request_data['lastName'], 'email': request_data['email'], 'password': hashed_password }
        users.append(newUser)
        print(users)
        return  "successful"

 


if __name__ == "__main__":
    app.run(debug=True , port = 4000)




#task 
   #is to use jwt with a single dictionary and try req using postman
   #then use mongoose and try using postman
   #then try with react
