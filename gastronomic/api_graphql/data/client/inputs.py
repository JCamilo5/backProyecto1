from graphene import ID
from graphene import String
from graphene import InputObjectType
from graphene.types.scalars import Boolean
from django.contrib.auth.hashers import make_password


# Create your inputs types here.


class CreateClientInput(InputObjectType):
    name = String(required=True)
    location = String(required=True)
    telephone = String(required=True)
    user = String(required=True)
    password = String(required=True)
    typeU = String(required=True)
    stateU = Boolean(required=True)

class UpdateClientInput(InputObjectType):
    id = ID(required=True)
    name = String()
    location = String()
    telephone = String()
    user = String()
    password = String()
    typeU = String()
    stateU = Boolean()

class DeleteClientInput(InputObjectType):
    id = ID(required=True)