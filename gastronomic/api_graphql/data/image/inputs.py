from graphene import (
    ID,
    String,
    InputObjectType
)

from graphene_file_upload.scalars import Upload

# Create your inputs types here.


class CreateImageInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la creación de imagenes
    """
    image = Upload(required=True)

    # Relaciones
    product_id = ID(required=True)


class UpdateImageInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la actualización de imagenes
    """
    id = ID(required=True)
    url = Upload(required=True) 
    
    # Relaciones
    product_id=ID()