import re
from flask import Flask, render_template, request, json, make_response, jsonify
from flask_cors import CORS
# from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt import jwt
from datetime import datetime, timedelta
# from flask_bcrypt import Bcrypt
from bson import ObjectId
from functools import wraps
from graphene.types import mutation
from mongoengine import connect
from graphene import ObjectType, String, Schema, Field,List, ID
from flask_graphql import GraphQLView
from src.user.api.query import UserQuery
from src.user.api.mutation import MyMutations
from src.user.data.model import User


app = Flask(__name__)
CORS(app)
# bcrypt = Bcrypt(app)


app.config['SECRET_KEY'] = "randomsecretkey"

connect(host="mongodb://127.0.0.1:27017/user_service_database")



schema = Schema(query=UserQuery, mutation=MyMutations)
# print(schema)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql-query',
    schema=schema, graphiql=True
))



# test route
@app.route('/')
def hello_world():
    return 'Hello, World!'


#signup route
@app.route('/auth/signup', methods=["POST"])
def Signup():
     
    if request.method == "POST":
        
        request_data = json.loads(request.data)
        

         
        user = User(
            first_name=request_data["firstName"], 
            last_name =request_data["lastName"], 
            email =request_data["email"],
            password = request_data["password"]
             )
        print(user)
        user.save()

        return make_response('Successfully registered.', 201)

 
if __name__ == "__main__":
    app.run(debug=True , port = 4000)




