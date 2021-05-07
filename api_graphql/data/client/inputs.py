from graphene import InputObjectType
from graphene.types.scalars import ID
from graphene.types.scalars import String
from graphene.types.scalars import Boolean

# Create your inputs types here.


class CreateClientInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios para la 
    creacion de clientes
    """

    email = String(required=True)
    password = String(required=True)
    names = String(required=True)
    lastnames = String(required=True)
    location = String(required=True)
    telephone = String(required=True)
    license_plate = String()


class UpdateClientInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la actualización de cliente
    """
    
    id = ID(required=True)
    password = String()
    is_active = Boolean()

class RememberPasswordInput(String):
    """
    Clase que encapsula los datos necesarios
    para la actualización de cliente
    """
    
    email = String(required=True)
