from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Contact
from  django.contrib import messages
from django.core.mail import send_mail

# Create your views here.

def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        #---------------------------------------------------
        # Проверка пользовтелия отправлял ли он сообщение
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'Вы уже отправляли это сообщение')
                return redirect('/cars/' + car_id)

        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id, first_name=first_name, last_name=last_name,
                          customer_need=customer_need, city=city, state=state, email=email, phone=phone, message=message)
        contact.save()
        messages.success(request, 'Ваш запрос был отправлен, мы свяжемся с вами')

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        send_mail(
            'Новое собшение от сайта Автомобилей',
            'Вы получили новое письмо', + car_title + 'Please login to your admin'
            'from@example.com',
            [admin_email],
            fail_silently=False
        )

        return  redirect('/cars/'+car_id)