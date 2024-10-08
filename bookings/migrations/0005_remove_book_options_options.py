# Generated by Django 4.2.14 on 2024-07-29 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_alter_book_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='options',
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('booking', models.ManyToManyField(to='bookings.book')),
            ],
        ),
    ]
