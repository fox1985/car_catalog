from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from cars import views



urlpatterns = [
    path('', views.cars, name='cars'),
    path('<int:id>', views.car_detail, name='car_detail'),
    path('search', views.search, name='search'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
