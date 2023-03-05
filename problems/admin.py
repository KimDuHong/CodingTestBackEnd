from django.contrib import admin

# Register your models here.
from .models import Problem

# Register your models here.
# @admin.register(Answer)


@admin.register(Problem)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("id",)
