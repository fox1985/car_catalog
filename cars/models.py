from datetime import datetime
from ckeditor.fields import RichTextField
from django.db import models



# Create your models here.



class Car(models.Model):
    state_choice = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )
    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r, r))

    features_choices = (
        ('Круиз-контроль', 'Круиз-контроль'),
        ('Аудио интерфейс', 'Аудио интерфейс'),
        ('Подушки безопасности', 'Подушки безопасности'),
        ('Кондиционер', 'Кондиционер'),
        ('Подогрев сидений', 'Подогрев сидений'),
        ('Аварийная система', 'Аварийная система'),
        ('Парковщик', 'Парковщик'),
        ('Усилитель рулевого управления', 'Усилитель рулевого управления'),
        ('Камера заднего вида', 'Камера заднего вида'),
        ('Непосредственный Впрыск Топлива', 'Непосредственный Впрыск Топлива'),
        ('Автоматический Запуск Остановка', 'Автоматический Запуск Остановка'),
        ('Ветроотражатель', 'Ветроотражатель'),
        ('Телефонная трубка Bluetooth', 'Телефонная трубка Bluetooth'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    car_title = models.CharField(max_length=255, verbose_name='Загаловак')
    state = models.CharField(choices=state_choice, max_length=100, verbose_name='города')
    city = models.CharField(max_length=100, verbose_name='Город')
    color = models.CharField(max_length=100, verbose_name='Цвет')
    model = models.CharField(max_length=100, verbose_name='Модель')
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=100, verbose_name='состояние')
    price = models.IntegerField(verbose_name='Цена')
    old_qina = models.IntegerField(verbose_name='Старая цина', blank=True, default=0)
    description = RichTextField()
    car_photo = models.ImageField(upload_to='car_photos/%Y/%m/%d/', verbose_name='Фото авто')
    car_photo_1 = models.ImageField(upload_to='car_photos/%Y/%m/%d/', blank=True, verbose_name='Фото авто')
    car_photo_2 = models.ImageField(upload_to='car_photos/%Y/%m/%d/', blank=True, verbose_name='Фото авто')
    car_photo_3 = models.ImageField(upload_to='car_photos/%Y/%m/%d/', blank=True, verbose_name='Фото авто')
    car_photo_4 = models.ImageField(upload_to='car_photos/%Y/%m/%d/', blank=True, verbose_name='Фото авто')
    features = models.CharField(choices=features_choices, max_length=100, verbose_name='особенности')
    body_style = models.CharField(max_length=100, verbose_name='Тип автомабиля')
    engine = models.CharField(max_length=100, verbose_name='двигатель')
    transmission = models.CharField(max_length=100, verbose_name='коробка передач')
    interior = models.CharField(max_length=100, verbose_name='интерьер')
    miles = models.IntegerField(verbose_name='миль')
    doors = models.CharField(choices=door_choices, max_length=10, verbose_name='двери')
    passengers = models.IntegerField(verbose_name='пассажиры')
    vin_no = models.CharField(max_length=100, verbose_name='Номер')
    milage = models.IntegerField(verbose_name='пробег')
    fuel_type = models.CharField(max_length=50, verbose_name='тип топлива')
    fuel_consumption = models.CharField(max_length=255, verbose_name='Расход топлива', blank=True)
    on_of_owners = models.CharField(max_length=100, verbose_name='от имени владельцев')
    is_featured = models.BooleanField(default=False,verbose_name='Опубликовано')
    created_data = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Дата создания обявления')


    class Meta:
        verbose_name = 'Авто'
        verbose_name_plural = 'Автомобили'


    def __str__(self):
        return self.car_title

