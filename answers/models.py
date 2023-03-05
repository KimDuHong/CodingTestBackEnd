from django.db import models
from common.models import CommonModel

# Create your models here.
class Answer(CommonModel):
    problem = models.ForeignKey(
        "problems.problem",
        on_delete=models.CASCADE,
        related_name="answer",
    )
    commentary = models.TextField()


class Language(CommonModel):
    class LanguageChoices(models.TextChoices):
        JAVASCRIPT = ("javascript", "자바스크립트")
        PYTHON = ("python", "파이썬")

    answer = models.OneToOneField(
        "answers.Answer",
        on_delete=models.CASCADE,
        related_name="answer",
    )

    language = models.CharField(
        max_length=10,
        choices=LanguageChoices.choices,
    )
    code = models.TextField()
