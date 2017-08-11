from django.contrib import admin
from .models import Main

@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ['id','name','image1']
