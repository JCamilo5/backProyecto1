from django.urls import path  
from accounts import views
urlpatterns = [  
        path('activate/<uidb64>/<token>/',views.activate, name='activate'),  
]
