from django.contrib.auth import login
from django.core.cache import cache
from django.contrib import messages
from users.models import UserPhone
import random
import string
from django.shortcuts import render, redirect


def sendsms(request):
    if request.method == "POST":
        phone_number = request.POST.get("phone_number")
        request.session["phone_number"] = phone_number
        code = ''.join(random.choices(
                string.ascii_uppercase + string.digits,
                k=6
            ))
        cache.set(f"sms_{phone_number}", code, timeout=300)
        print(f"Код для номера {phone_number}: {code}")
        return redirect("/check_code/")
    return render(request, "phone/index.html",)


def check_code(request):
    phone_number = request.session.get("phone_number")
    if request.method == "POST":
        phone_number = request.POST.get("phone_number")
        saved_code = cache.get(f"sms_{phone_number}")
        code = request.POST.get("code")
        if saved_code != code:
            phone_number = request.session.get("phone_number")
            messages.error(request, "Не тот код")
            return render(request, "phone/index_code.html")
        invite_code = ''.join(random.choices(
            string.ascii_uppercase + string.digits,
            k=6
        ))
        user, created = UserPhone.objects.get_or_create(
            phone_number=phone_number,
            defaults={
                "username": phone_number,
                "invite_code": invite_code,
            }
        )
        if created:
            ref_code = invite_code
        else:
            ref_code = user.invite_code
        context = {
            "phone_number": phone_number,    
            "invite_code": ref_code,
        }   
        return render(request, "phone/home.html", context)
    return render(request, "phone/index_code.html", {'phone_number': phone_number})

