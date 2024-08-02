# Generated by Django 4.2.14 on 2024-08-02 14:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0007_book_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='book',
            name='options',
            field=models.IntegerField(choices=[(0, 'Finger Food'), (1, 'Snacks'), (2, 'Craft Beer'), (3, 'Soda')]),
        ),
    ]
