from django.core.exceptions import ImproperlyConfigured
from graphene import Field
from graphene import Mutation

from orders.models import Report
from api_graphql.data.report.types import ReportNode
from api_graphql.data.report.inputs import CreateReportInput
from api_graphql.utils import delete_attributes_none
from api_graphql.utils import transform_global_ids
from django.db import connection

import datetime

class CreateReport(Mutation):
    """Clase para crear una reporte"""

    report = Field(ReportNode)

    class Arguments:
        input = CreateReportInput(required=True)

    def mutate(self, info, input):
        #input = delete_attributes_none(**vars(input))


        cursor = connection.cursor()
        cursor.execute("""select e.name, oo.date, pp.payment_value  from enterprises_enterprise e
                        INNER JOIN products_product pr on pr.enterprise_id == e.id
                        INNER JOIN orders_detail od on od.product_id == pr.id
                        INNER JOIN orders_order oo on oo.id == od.order_id
                        INNER JOIN deliveries_delivery dd on dd.order_id == oo.id
                        INNER JOIN payments_payment pp on pp.delivery_id == dd.id where e.id="""+input.get('id_interprise')+""" and dd.status = 1
                        """)
        rawData =cursor.fetchall()
        result = []
        input['report_information']="Establecimiento: "+list(rawData[0])[0]

        for r in rawData:
            input['report_information']= input['report_information']+"Fecha: "+list(r)[1].strftime('%d-%m-%Y')+" Valor Pedido: "+str(list(r)[2])
            result.append(list(r))
        #contexto = {'consultas': result}
        #print(result)

        report = Report.objects.create(**input)

        return CreateReport(report=report)

