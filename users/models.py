from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(
        max_length=100,
        unique=True,
    )
    first_name = models.CharField(max_length=10, editable=False)
    last_name = models.CharField(max_length=10, editable=False)
