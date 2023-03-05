from django.db import models
from common.models import CommonModel

# Create your models here.
class Problem(CommonModel):
    description = models.TextField()
    type = models.CharField(
        max_length=10,
    )
    level = models.IntegerField()
