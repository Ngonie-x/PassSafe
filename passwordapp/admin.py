from django.contrib import admin
from .models import PasswordModel

# Register your models here.

class PasswordModelAdmin(admin.ModelAdmin):
    list_display =['site_url', 'username']

admin.site.register(PasswordModel, PasswordModelAdmin)