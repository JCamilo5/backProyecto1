from graphene import ID
from graphene import String
from graphene import InputObjectType

# Create your inputs types here.


class CreateEnterpriseInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la creación de empresas
    """
    name = String(required=True)
    historical_review = String()
    location = String(required=True)
    business_hours = String(required=True)


class UpdateEnterpriseInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la actualización de empresas
    """
    id = ID(required=True)
    name = String()
    historical_review = String()
    location = String()
    business_hours = String()
