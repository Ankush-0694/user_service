from graphene.types.scalars import Boolean
from src.user.logic.logic import UserLogic
from graphene import ObjectType, Mutation, String, Field
from src.user.api.schema import User


class createUser(Mutation):
    class Arguments:
        first_name = String()
        last_name = String()
        email = String()
        password = String()
        role=String(default_value="user")
    ok = Boolean()  # why it is recommended
    add_user = Field(User)
    def mutate(self, _info, first_name, last_name, email, password, role):
        ok = True
        user =  UserLogic.create(first_name, last_name, email, password,role)
        # print(user)
        return createUser(add_user=user, ok=ok) #### can we return just user object like nodejs

       



class UserMutations(ObjectType):
    create_user = createUser.Field()



 ## mutation will be below , in below mutation can we just return firstName without using addUser object
        # mutation{
        #     createUser(email:"abbb", firstName:"b", lastName:"c", password:"d"){
        #         addUser{
        #         firstName
        #         lastName
        #         email
        #         }
        #     }
        # }