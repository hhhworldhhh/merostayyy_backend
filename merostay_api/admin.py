from django.contrib import admin
from .models import hotel_info

class hotel_info_admin(admin.ModelAdmin):
    list_display=["hotel_name","hotel_address","hotel_city"]

admin.site.register(hotel_info,hotel_info_admin)
