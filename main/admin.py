from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['username', "pk", 'first_name', 'last_name', 'phone_number', 'email']
    search_fields = ['username', "pk", 'first_name', 'last_name', 'phone_number', 'email']
    
