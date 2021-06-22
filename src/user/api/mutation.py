from graphene.types.scalars import Boolean
from src.user.logic.logic import UserLogic
from graphene import ObjectType, Mutation, String, Field
from src.user.api.Fields import UserField


class CreateUser(Mutation):
    user = Field(UserField)
    ok=Boolean();
    class Arguments:
        first_name = String()
        last_name = String()
        email = String()
        password = String()
        role=String(default_value="user")
    
    def mutate(self, _info, first_name, last_name, email, password, role):
        ok=True
        created_user =  UserLogic.create(first_name, last_name, email, password,role)
        return CreateUser(user=created_user, ok=ok) 


class UserMutations(ObjectType):
    create_user = CreateUser.Field()

