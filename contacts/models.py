from django.db import models
from  datetime import datetime
# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    car_id = models.IntegerField(verbose_name='Авто id')
    customer_need = models.CharField(max_length=100, verbose_name='потребность клиента')
    car_title = models.CharField(max_length=100, verbose_name='Загаловак')
    city = models.CharField(max_length=100, verbose_name='Город')
    state = models.CharField(max_length=100, verbose_name='Страна')
    email = models.EmailField(max_length=100, verbose_name='Почта')
    phone = models.CharField(max_length=100, verbose_name='Телефон')
    message = models.TextField(blank=True, verbose_name='Собщение')
    user_id = models.IntegerField(blank=True)
    create_date = models.DateTimeField(blank=True, default=datetime.now)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.email
