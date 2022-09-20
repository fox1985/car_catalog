from django.db import models

# Create your models here.

class Teams(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    designation = models.CharField(max_length=255, verbose_name='Описания')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение', blank=True)
    facebook_link = models.URLField(max_length=100, verbose_name='facebook ссылка', blank=True)
    twitter_link = models.URLField(max_length=100, verbose_name='twitter ссылка', blank=True)
    google_plus_link = models.URLField(max_length=100, verbose_name='google_plus ссылка', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Команду'
        verbose_name_plural = 'Наша команда'

    def __str__(self):
        return self.first_name