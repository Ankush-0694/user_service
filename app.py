from flask import Flask, request, json, make_response, jsonify
from flask_cors import CORS
from graphene.types.objecttype import ObjectType
from mongoengine import connect
from flask_graphql import GraphQLView
from src.admin.api.query import AdminQuery
from src.user.api.query import UserQuery
from src.user.api.mutation import UserMutations
from src.admin.api.mutation import AdminMutations
from graphene_federation import build_schema
from Constants.constants import *
from src.vendor.api.mutation import VendorMutations
from src.vendor.api.query import VendorQuery

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = secret_key

connect(host=mongo_url)


class Query(UserQuery ,AdminQuery,VendorQuery,   ObjectType):
    pass

class Mutation(UserMutations, AdminMutations, VendorMutations,  ObjectType):
    pass

schema = build_schema(query=Query, mutation=Mutation)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql-query',
    schema=schema, graphiql=True
))

# test route
@app.route('/')
def hello_world():
    return 'Hello, World!'
 
if __name__ == "__main__":
    app.run(debug=True , port = 4000)



# #signup route
# @app.route('/auth/signup', methods=["POST"])
# def Signup():
     
#     if request.method == "POST":
        
#         request_data = json.loads(request.data)
#         user = User(
#             first_name=request_data["firstName"], 
#             last_name =request_data["lastName"], 
#             email =request_data["email"],
#             password = request_data["password"]
#              )
#         print(user)
#         user.save()

#         return make_response('Successfully registered.', 201)


    # globals()[sys.argv[1]](sys.argv[2],sys.argv[3], sys.argv[4], sys.argv[5]) 
