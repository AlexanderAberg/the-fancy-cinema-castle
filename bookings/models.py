from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


SESSIONS = ((0, 'Action Movies'), (1, 'Comedy Movies'), (2, 'Drama Movies'),
            (3, 'Video Games'))
OPTIONS = ((0, 'Finger Food'), (1, 'Snacks'), (2, 'Craft Beer'), (3, 'Soda'))


# Create your models here.
class Book(models.Model):
    # The Booking Manager
    date = models.DateTimeField(default=timezone.now)
    amount = models.PositiveIntegerField(validators=[MinValueValidator(2),
                                                     MaxValueValidator(20)])
    session_type = models.IntegerField(choices=SESSIONS, default='3')
    options = models.IntegerField(choices=OPTIONS)
    wishes = models.TextField(
        blank=True, verbose_name='Wishes & Information', max_length=500)

    booker = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bookings", null=True
    )

    def __str__(self):
        return f'{self.booker}, {self.date}'
