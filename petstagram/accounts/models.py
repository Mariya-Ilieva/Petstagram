from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator


def validate_name(value):
    if not value.isalpha():
        raise ValidationError('Name must contain only alphabetical letters.')


class PetstagramUser(AbstractUser):
    CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Do not show', 'Do not show'),
    ]
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, validators=[MinValueValidator(2), validate_name, ])
    last_name = models.CharField(max_length=30, validators=[MinValueValidator(2), validate_name, ])
    profile_picture = models.URLField()
    gender = models.CharField(max_length=25, choices=CHOICES)
