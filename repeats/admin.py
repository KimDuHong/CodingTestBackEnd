from django.contrib import admin
from .models import Repeat

# Register your models here.

# Register your models here.
# @admin.register(Answer)


@admin.register(Repeat)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("id",)
