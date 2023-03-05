from django.contrib import admin
from .models import Answer, Language

# Register your models here.
# @admin.register(Answer)


@admin.register(Answer, Language)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("id",)
