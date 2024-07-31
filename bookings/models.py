from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

SESSIONS= ((0, 'Action Movies'), (1, 'Comedy Movies'), (2, 'Drama Movies'), (3, 'Video Games'))

# Create your models here.
class Book(models.Model):
    #The Booking Manager
    date = models.DateTimeField()
    amount = models.PositiveIntegerField(validators=[MinValueValidator(2), MaxValueValidator(20)])
    session_type = models.IntegerField(choices=SESSIONS, default='3')
 #   options = models.ManyToManyField(Option)
    wishes = models.TextField(
        blank=True, verbose_name='Wishes & Information', max_length=500)

    booker = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bookings", null = True
    ) 

    def __str__(self):
        return f'{self.booker}, {self.date}'
