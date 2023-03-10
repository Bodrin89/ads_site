# Generated by Django 4.1.7 on 2023-03-01 08:42

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_birth_date_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[users.validators.not_rambler]),
        ),
    ]
