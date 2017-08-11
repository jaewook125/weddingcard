from django.contrib import admin
from .models import MainComment, Comment

@admin.register(MainComment)
class MainAdmin(admin.ModelAdmin):
    list_display = ['id','name','image1']

@admin.register(Comment)
class MainAdmin(admin.ModelAdmin):
    list_display = ['id','user','password','content']
