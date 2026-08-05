from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class EnglishLevel(models.TextChoices):
        A1 = "A1", "Beginner (A1)"
        A2 = "A2", "Elementary (A2)"
        B1 = "B1", "Intermediate (B1)"
        B2 = "B2", "Upper-Intermediate (B2)"
        C1 = "C1", "Advanced (C1)"

    english_level = models.CharField(
        max_length=2,
        choices=EnglishLevel.choices,
        default=EnglishLevel.A1,
    )
    is_moderator = models.BooleanField(default=False)

    def __str__(self):
        return self.username