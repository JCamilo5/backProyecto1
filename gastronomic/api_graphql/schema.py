from graphene import ObjectType
from graphene.relay import Node
import graphene



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
from .data.report.report import Report, Reports

from .data.enterprise.mutations import (
    CreateEnterprise,
    UpdateEnterprise,
    DeleteEnterprise
)
from .data.client.mutations import (
    CreateClient,
    UpdateClient,
    RememberPasswordClient,
    ActivateClient
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

# Schema definition



import graphql
from datetime import datetime
from datetime import timedelta
from payments.models import Payment



class Query(ObjectType):
    """Endpoint para consultar registros"""

    reports = graphene.Field(Reports, enterprise=graphene.String(), report_type=graphene.Int())
    def resolve_reports(self, info: graphql.ResolveInfo,enterprise,report_type):

        current_date= datetime.now()
        #reporte diario
        if(report_type==1):
            start_date=current_date-timedelta(hours=24)
        elif(report_type ==2):
            #reporte semanal
            start_date=current_date-timedelta(days=7)
        elif(report_type ==3):
            #reporte mensual
            start_date=current_date-timedelta(days=30)

        query_reports=Payment.objects.filter(delivery__delivery_time__range=[start_date,current_date],delivery__order__details__product__enterprise=enterprise,delivery__status="1").values('delivery__order__details__product__enterprise__name' ,'delivery__delivery_time','payment_value').distinct()

        reports_as_obj_list = [] 
        
        total=0
        for query_report in query_reports: 
            report = Report(query_report.get('delivery__delivery_time').strftime(("%d-%m-%Y %H:%M:%S")),query_report.get('payment_value')) # Creates a report object where key=key and header=value
            reports_as_obj_list.append(report)
            total=report.payment_value+total
        object_reports = Reports(query_report.get('delivery__order__details__product__enterprise__name'),report_type,reports_as_obj_list,total)
        return object_reports

    
    
    
    
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
    activate_client = ActivateClient.Field()
    
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
