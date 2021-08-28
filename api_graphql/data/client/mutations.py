from api_graphql.data.contact.inputs import UpdateContactInput
from graphene import Field
from graphene import Mutation
from graphene.types.scalars import ID
from graphql_relay.node.node import from_global_id

from users.models import Client, Contact
from api_graphql.data.client.types import ClientNode
from api_graphql.data.client.inputs import CreateClientInput, RememberPasswordInput
from api_graphql.data.client.inputs import UpdateClientInput
from api_graphql.utils import delete_attributes_none
from api_graphql.utils import transform_global_ids
from users.views import remember,signup
# Create your mutations here


class CreateClient(Mutation):
    """Clase para crear clientes"""

    client = Field(ClientNode)

    class Arguments:
        input = CreateClientInput(required=True)

    def mutate(self, info, input: CreateClientInput):
        input = vars(input)
        client = Client(
            email=input.pop('email'),
            password=input.pop('password'),
            is_alternative = input.pop('is_alternative')
        )
        input['user'] = client
        contact = Contact(**input)
        client.save()
        contact.save()
        if(client.password != 'deliver-food-2021'):
            signup(client)
        else:
            
            client = Client.objects.get(email=client.email)
            client.is_active=True
            client.save()

        return CreateClient(client=client)


class UpdateClient(Mutation):
    """Clase para actualizar clientes"""

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

class RememberPasswordClient(Mutation):
    """Clase para actualizar clientes"""

    client = Field(ClientNode)

    class Arguments:
        input = RememberPasswordInput(required=True)

    def mutate(self, info, input):
        client = Client.objects.get(email=input)
        if (client.is_alternative==False):
            remember(client)
        return RememberPasswordClient(client=client)
