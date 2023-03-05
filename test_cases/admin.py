from django.contrib import admin
from .models import Test_Case

# Register your models here.

# Register your models here.
# @admin.register(Answer)


@admin.register(Test_Case)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("id",)
