from django.contrib import admin
from  .models import Car, Features
from django.utils.html import format_html

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="60" style="border-radius:80px "/>'.format(object.car_photo.url))

    thumbnail.short_description = 'Photo'

    list_display = ( 'thumbnail', 'car_title', 'price', 'old_qina', 'state', 'city', 'color', 'model', 'year', 'fuel_type', 'on_of_owners', 'is_featured',)
    list_editable = ('is_featured', 'price', 'old_qina')
    search_fields = ('car_title', 'city', 'model',  'color',)
    list_filter = ('year', 'fuel_type')

admin.site.register(Car,CarAdmin)
admin.site.register(Features)
