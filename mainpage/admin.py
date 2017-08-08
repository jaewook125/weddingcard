from django.contrib import admin
from .models import Main, Name

@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ('name','image','created_at','updated_at')

@admin.register(Name)
class NameAdmin(admin.ModelAdmin):
    list_display = ('husband','wife','content')
