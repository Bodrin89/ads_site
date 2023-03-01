# Generated by Django 4.1.5 on 2023-02-28 08:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]