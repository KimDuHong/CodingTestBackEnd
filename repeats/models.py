from django.db import models
from common.models import CommonModel

# Create your models here.
class Repeat(CommonModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    problem = models.ForeignKey(
        "problems.Problem",
        on_delete=models.CASCADE,
    )
