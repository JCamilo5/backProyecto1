import graphene

import datetime
from datetime import datetime
from datetime import timedelta
from payments.models import Payment

class Report(graphene.ObjectType):   
    report_date = graphene.String()
    payment_value = graphene.Int()

class Reports(graphene.ObjectType):
    token = graphene.String()  
    enterprise= graphene.ID()       
    start_date = graphene.DateTime()
    final_date = graphene.DateTime()
    report_list = graphene.List(Report)
    total_value = graphene.Float()

def get_query_report(enterprise,start_date,final_date):
    #fecha actual
        current_date= datetime.now()
        #fecha de cierre del establecimiento obtenida de la bd
        close_date= datetime.now()-timedelta(hours=1)
        
        if(current_date.date()==final_date):
            if(close_date>current_date):
                final_date=final_date-timedelta(days=1)

        query_reports=Payment.objects.filter(delivery__delivery_time__range=[start_date,final_date],delivery__order__details__product__enterprise=enterprise.pk,delivery__status="1").values('delivery__order__details__product__enterprise__name' ,'delivery__delivery_time','payment_value').distinct()
        return query_reports
def get_data_report(query_reports,start_date,final_date):
    
    reports_as_obj_list = [] 
    total=0
    try:
        for query_report in query_reports: 
            report = Report(query_report.get('delivery__delivery_time'),query_report.get('payment_value')) 
            reports_as_obj_list.append(report)
            total=report.payment_value+total

        object_reports = Reports(query_report.get('delivery__order__details__product__enterprise__name'),start_date, final_date, reports_as_obj_list,total)
        return object_reports
    except: 
        return None

