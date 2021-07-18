from flask import Flask, request, json, make_response, jsonify
from flask_cors import CORS
from graphene.types.objecttype import ObjectType
from mongoengine import connect
from flask_graphql import GraphQLView
from graphene_federation import build_schema
from Constants.constants import *
from src.user.api.query import AuthQuery, UserQuery, VendorQuery, AdminQuery
from src.user.api.mutation import UserMutations, AdminMutations, VendorMutations

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = secret_key

connect(host=mongo_url)


class Query(UserQuery ,AdminQuery,VendorQuery, AuthQuery,    ObjectType):
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


