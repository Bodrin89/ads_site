from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.db.models import CASCADE

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(
                            unique=True,
                            validators=[MinLengthValidator(limit_value=5),
                                        MaxLengthValidator(limit_value=10)],
                            blank=True,
                            null=True
                            )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, validators=[MinLengthValidator(10)])
    price = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images', null=False, default=None)
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.name
