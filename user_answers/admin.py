from django.contrib import admin
from .models import User_Answer

# Register your models here.
@admin.register(User_Answer)
class User_Answer_Admin(admin.ModelAdmin):
    list_display = ("id",)
