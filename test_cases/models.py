from django.db import models
from common.models import CommonModel

# Create your models here.
class Test_Case(CommonModel):
    problem = models.ForeignKey(
        "problems.Problem",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    input_value = models.CharField(max_length=50)
    output_value = models.CharField(max_length=50)
