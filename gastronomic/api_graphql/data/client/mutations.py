from graphene import Field
from graphene import Mutation

from users.models import Client
from api_graphql.data.client.types import ClientNode
from api_graphql.data.client.inputs import CreateClientInput
from api_graphql.data.client.inputs import UpdateClientInput
from api_graphql.utils import delete_attributes_none
from api_graphql.utils import transform_global_ids
# Create your mutations here


class CreateClient(Mutation):
    client = Field(ClientNode)

    class Arguments:
        input = CreateClientInput(required=True)

    def mutate(self, info, input: CreateClientInput):
        client = Client.objects.create(**vars(input))

        return CreateClient(client=client)

class UpdateClient(Mutation):
    client = Field(ClientNode)
    
    class Arguments:
        input = UpdateClientInput(required=True)

    def mutate(self, info, input):
        # Elimina nulos y transforma el id
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        
        Client.objects.filter(pk=input.get('id')).update(**input)
        client = Client.objects.get(pk=input.get('id'))

        return UpdateClient(client=client)

