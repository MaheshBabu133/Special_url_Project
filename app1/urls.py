from app1.views import*
from django.urls import path
app_name='something'
urlpatterns=[
    path('Mahesh/',Mahesh,name='Mahesh'),
    path('Afrin/',Afrin,name='Afrin'),
]