from django.urls import path
from .views import SendSMSView, VerifyCodeView

urlpatterns = [
    path('send-sms/', SendSMSView.as_view(), name='send_sms'),
    path('verify/', VerifyCodeView.as_view(), name='verify'),
]