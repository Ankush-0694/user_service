from flask import Flask
from flask_cors import CORS
from graphene.types.objecttype import ObjectType
from mongoengine import connect
from flask_graphql import GraphQLView
from graphene_federation import build_schema
from Constants.constants import SECRET_KEY, MONGO_URL, SENDGRID_API_KEY, SENDER_EMAIL
from flask_mail import Mail, Message
from src.user.api.query import AuthQuery, UserQuery
from src.user.api.mutation import UserMutations, VendorMutation

app = Flask(__name__)
CORS(app)

""" For storing the secret - JWT """
app.config['SECRET_KEY'] = SECRET_KEY

""" Configuration for mail """
app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'apikey'
app.config['MAIL_PASSWORD'] = SENDGRID_API_KEY
app.config['MAIL_DEFAULT_SENDER'] = SENDER_EMAIL

mail = Mail(app)


connect(host=MONGO_URL)

class Query(UserQuery , AuthQuery,    ObjectType):
    pass

class Mutation(UserMutations, VendorMutation,   ObjectType):
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



