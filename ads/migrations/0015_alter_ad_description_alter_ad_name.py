# Generated by Django 4.1.5 on 2023-02-28 11:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0014_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='name',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
