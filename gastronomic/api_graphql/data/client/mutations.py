from graphene import Field
from graphene import Mutation
from graphene.types.scalars import ID

from enterprises.models import Enterprise
from products.models import Product
from orders.models import Detail
from orders.models import Order
from datetime import datetime
from datetime import timedelta
from payments.models import Payment


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
        tipo=3

        fechaActual= datetime.now()
        #reporte diario
        if(tipo==1):
            fechaInicio=fechaActual-timedelta(hours=24)
        elif(tipo ==2):
            #reporte semanal
            fechaInicio=fechaActual-timedelta(days=7)
        elif(tipo ==3):
            #reporte mensual
            fechaInicio=fechaActual-timedelta(days=30)
        print(fechaInicio)
        print(fechaActual)

        
        
        
        
        pagos=Payment.objects.filter(delivery__delivery_time__range=[fechaInicio,fechaActual],delivery__order__details__product__enterprise='2').values('delivery__order__details__product__enterprise__name','delivery__delivery_time','payment_value')

        print(pagos)
        



        

        """
        input = vars(input)
        client = Client(
            email=input.pop('email'),
            password=input.pop('password'),
            is_alternative = input.pop('is_alternative')
        )
        input['user'] = client
        contact = Contact(**input)
        client.is_active=False
        client.save()
        contact.save()
        if(client.password != 'deliver-food-2021'):
            signup(client, info.context)
        else:
            client = Client.objects.get(email=client.email)
            client.is_active=True
            client.save()

        return CreateClient(client=client)
        """
        return None


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
            remember(client, info.context)
        return RememberPasswordClient(client=client)
