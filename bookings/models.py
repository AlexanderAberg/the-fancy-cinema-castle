from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    date = models.DateTimeField()
    amount = models.PositiveIntegerField(validators=[MinValueValidator(2.0), MaxValueValidator(20.0)])
