from django.contrib import admin

from models import *


class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'rating', 'website')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'work')



admin.site.register(Client, ClientAdmin)
admin.site.register(Hotel, HotelAdmin)


