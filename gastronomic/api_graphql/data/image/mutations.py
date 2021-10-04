from products.models import Product
from graphene import Field
from graphene import Mutation
import graphene
from graphene.types.scalars import ID
from graphql import GraphQLError
from graphql_relay.node.node import from_global_id

from products.models import Image
from api_graphql.data.image.types import ImageNode
from api_graphql.data.image.inputs import CreateImageInput
from api_graphql.data.image.inputs import UpdateImageInput
from api_graphql.utils import delete_attributes_none
from api_graphql.utils import transform_global_ids
from graphene_file_upload.scalars import Upload
from django.core.files.storage import default_storage


# Create your mutations here


class CreateImage(Mutation):
    class Arguments:
        product = ID(required=True)
        file = Upload(required=True)        

    success = graphene.Boolean()

    def mutate(self, info, product, file, **kwargs):
        product=from_global_id(product)[1]
        productC = Product.objects.get(pk=product)
        newImage = Image(url = file, product=productC)
        newImage.save()    
        newImage.url.name=newImage.url.url;
        newImage.save()    
        return CreateImage(success=True)



class UpdateImage(Mutation):
    """Clase para actualizar imagenes"""
    image = Field(ImageNode)

    class Arguments:
        input = UpdateImageInput(required=True)

    def mutate(self, info, input):
        # Elimina nulos y transforma el id
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        image = Image.objects.get(pk=input.get('id'))
        image.url=input.get("url")
        image.save()
        image.url.name=image.url.url;
        image.save()          
        return UpdateImage(image=image)


class DeleteImage(Mutation):
    """Clase para eliminar imagenes"""
    image = Field(ImageNode)

    class Arguments:
        input = ID(required=True)

    def mutate(self, info, input):
        # Transforma el id
        input = from_global_id(input)[1]

        try:
            image = Image.objects.get(pk=input)
            Image.objects.filter(pk=input).delete()
        except Image.DoesNotExist:
            raise GraphQLError('Image does not delete')

        return CreateImage(image=image)




