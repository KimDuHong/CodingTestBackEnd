from django.db import models
from common.models import CommonModel

# Create your models here.
class User_Answer(CommonModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    problem = models.ForeignKey(
        "problems.Problem",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    language = models.CharField(max_length=10)
    code = models.TextField()
    is_solved = models.BooleanField(default=False)
    # solved_time = models.DateTimeField()
