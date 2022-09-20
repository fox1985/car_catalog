from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from pages import views



urlpatterns = [
    path('', views.home, name='home'),

    path('about', views.about, name='about'),

    path('services', views.services, name='services'),

    path('contact', views.contact, name='contact'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
