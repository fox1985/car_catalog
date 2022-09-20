
from django.shortcuts import render, redirect
from .models import Teams
from cars.models import Car
from  django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    teams = Teams.objects.all()
    featured_cars = Car.objects.order_by('-created_data').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_data')
    #search_fieds = Car.objects.values('model', 'year', 'city', 'body_style') #Поиск по полям

    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()

    context = {'teams' : teams, 'featured_cars' : featured_cars, 'all_cars' : all_cars,

            'model_search' : model_search,
            'city_search': city_search,
            'year_search' : year_search,
            'body_style_search' : body_style_search,



            }
    return render(request, 'pages/home.html', context)


def about(request):
    teams = Teams.objects.all()
    context = {'teams': teams}
    return render(request, 'pages/about.html', context)

def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'Увас новае собщение Контроль над сайтом' + subject
        messge_body = 'Name ' + name, '. Email: ' + email + '. Phone: '  + phone + '. Message: ' + message

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        send_mail(
            email_subject,
             messge_body,
            'from@example.com',
            [admin_email],
            fail_silently=False
        )
        messages.success(request, 'Спасибо собщение отправлино')
        return redirect('contact')

    return render(request, 'pages/contact.html')