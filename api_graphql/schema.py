from typing_extensions import Required
import graphene
from api_graphql.data.report.report import Report
from datetime import timedelta
import datetime
import graphql

from payments.models import Payment
from graphene import ObjectType

from graphene.relay import Node
from graphene_django.filter import DjangoFilterConnectionField

from .data.user.types import UserNode
from .data.order.types import OrderNode
from .data.client.types import ClientNode
from .data.detail.types import DetailNode
from .data.contact.types import ContactNode
from .data.payment.types import PaymentNode
from .data.courier.types import CourierNode
from .data.product.types import ProductNode
from .data.manager.types import ManagerNode
from .data.delivery.types import DeliveryNode
from .data.enterprise.types import EnterpriseNode
from .data.management.types import ManagementNode
from .data.review.types import ReviewNode
from .data.enterprise.mutations import (
    CreateEnterprise,
    UpdateEnterprise,
    DeleteEnterprise
)
from .data.client.mutations import (
    CreateClient,
    UpdateClient,
    RememberPasswordClient
)
from .data.courier.mutations import (
    CreateCourier,
    UpdateCourier
)
from .data.contact.mutations import (
    CreateContact,
    UpdateContact
)

from .data.detail.mutations import (
    CreateDetail,
    UpdateDetail,
    DeleteDetail
)
from .data.order.mutations import(
    CreateOrder,
    UpdateOrder,
    DeleteOrder
)
from .data.review.mutations import(
    CreateReview,
    UpdateReview
)

# Schema definition  # dictionary value
class Query(graphene.ObjectType):
    questionnaire = graphene.Field(Report, enterprise=graphene.String())
    def resolve_questionnaire(self, info: graphql.ResolveInfo,enterprise):
            tipo=enterprise

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
            pagos=Payment.objects.filter(delivery__delivery_time__range=[fechaInicio,fechaActual],delivery__order__details__product__enterprise='2').values('delivery__order__details__product__enterprise__name' ,'delivery__delivery_time','payment_value')
            
            sections_as_obj_list = [] # Used to return a list of Section types
            # Create a new Section object for each item and append it to list
            for pago in pagos: # Use sections.iteritems() in Python2
                section = Report(pago.get('delivery__order__details__product__enterprise__name'), pago.get('delivery__delivery_time'),pago.get('payment_value')) # Creates a section object where key=key and header=value
                sections_as_obj_list.append(section)

            # return sections
            return sections_as_obj_list
    delivery = Node.Field(DeliveryNode)
    courier = Node.Field(CourierNode)
    client = Node.Field(ClientNode)
    contact = Node.Field(ContactNode)
    enterprise = Node.Field(EnterpriseNode)
    order = Node.Field(OrderNode)
    product = Node.Field(ProductNode)
    manager = Node.Field(ManagerNode)
    detail = Node.Field(DetailNode)
    user = Node.Field(UserNode)
    management = Node.Field(ManagementNode)
    payment = Node.Field(PaymentNode)
    review = Node.Field(ReviewNode)

    all_deliveries = DjangoFilterConnectionField(DeliveryNode)
    all_couriers = DjangoFilterConnectionField(CourierNode)
    all_clients = DjangoFilterConnectionField(ClientNode)
    all_contacts = DjangoFilterConnectionField(ContactNode)
    all_enterprises = DjangoFilterConnectionField(EnterpriseNode)
    all_orders = DjangoFilterConnectionField(OrderNode)
    all_products = DjangoFilterConnectionField(ProductNode)
    all_managers = DjangoFilterConnectionField(ManagerNode)
    all_details = DjangoFilterConnectionField(DetailNode)
    all_users = DjangoFilterConnectionField(UserNode)
    all_management = DjangoFilterConnectionField(ManagementNode)
    all_payments = DjangoFilterConnectionField(PaymentNode)
    all_reviews = DjangoFilterConnectionField(ReviewNode)
    

class Mutation(ObjectType):
    """Endpoint para crear, actualizar y eliminar registros"""

    create_enterprise = CreateEnterprise.Field()
    update_enterprise = UpdateEnterprise.Field()
    delete_enterprise = DeleteEnterprise.Field()

    create_client = CreateClient.Field()
    update_client = UpdateClient.Field()
    remember_client = RememberPasswordClient.Field()
    
    create_courier = CreateCourier.Field()
    update_courier = UpdateCourier.Field()

    create_contact = CreateContact.Field()
    update_contact = UpdateContact.Field()

    create_detail = CreateDetail.Field()
    update_detail = UpdateDetail.Field()
    delete_detail = DeleteDetail.Field()

    create_order = CreateOrder.Field()
    update_order = UpdateOrder.Field()
    delete_order = DeleteOrder.Field()

    create_review = CreateReview.Field()
    update_review = UpdateReview.Field()

