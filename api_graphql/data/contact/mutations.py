from graphene import Field
from graphene import Mutation
from graphene.types.scalars import ID

from users.models import Contact
from api_graphql.data.contact.types import ContactNode
from api_graphql.data.contact.inputs import CreateContactInput
from api_graphql.data.contact.inputs import UpdateContactInput
from api_graphql.utils import delete_attributes_none
from api_graphql.utils import transform_global_ids
from graphql_relay.node.node import from_global_id

# Create your mutations here


class CreateContact(Mutation):
    """Clase para crear contactos"""

    contact = Field(ContactNode)

    class Arguments:
        input = CreateContactInput(required=True)

    def mutate(self, info, input: CreateContactInput):
        input = delete_attributes_none(**vars(input))
        contact = Contact.objects.create(**input)

        return CreateContact(contact=contact)


class UpdateContact(Mutation):
    """Clase para actualizar contactos"""

    contact = Field(ContactNode)

    class Arguments:
        input = UpdateContactInput(required=True)

    def mutate(self, info, input):
        # Elimina nulos y transforma el id
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        Contact.objects.filter(pk=input.get('id')).update(**input)
        contact = Contact.objects.get(pk=input.get('id'))

        return UpdateContact(contact=contact)
