# Generated by Django 3.0.8 on 2020-07-20 07:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garbage', '0002_user_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='garbage',
            name='Urgency',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]