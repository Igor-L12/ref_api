from django.urls import path
from .views import sendsms, check_code

urlpatterns = [
    path("", sendsms, name='index'),
    path("check_code/", check_code, name='code'),                             
]                              