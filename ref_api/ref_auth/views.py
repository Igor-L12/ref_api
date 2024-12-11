from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from users.models import UserPhone
import random
import time
import string


class SendSMSView(APIView):
    def post(self, request):
        phone_number = request.data.get("phone_number")
        if not phone_number:
            return Response({"Введите номер"}, status=status.HTTP_400_BAD_REQUEST)
        code = ''.join(random.choices(
            string.ascii_uppercase + string.digits,
            k=6
        ))
        cache.set(f"sms_{phone_number}", code, timeout=300)
        time.sleep(1.7)
        print(f"Код для номера {phone_number}: {code}")
        return Response({"Код был успешно отправлен"}, status=status.HTTP_200_OK)
    

class VerifyCodeView(APIView):
    def post(self, request):
        phone_number = request.data.get("phone_number")
        code = request.data.get("code")
        if not phone_number or not code:
            return Response({"Что-то не то"}, status=status.HTTP_400_BAD_REQUEST)
        saved_code = cache.get(f"sms_{phone_number}")
        if saved_code != code:
            return Response({"Не тот код"}, status=status.HTTP_400_BAD_REQUEST)
        invite_code = ''.join(random.choices(
            string.ascii_uppercase + string.digits,
            k=6
        ))
        user, created = UserPhone.objects.get_or_create(phone_number=phone_number, invite_code=invite_code)
        if created:
            user.save()
        return Response({"Подтверждено!"}, status=status.HTTP_200_OK)
