from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Recipe)
class Recipe_list(admin.ModelAdmin):
    list_display = ['id','name','desc','image']