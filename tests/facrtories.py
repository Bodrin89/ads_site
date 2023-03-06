import factory.django

from ads.models import Category, Ad
from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    email = factory.Faker("email")


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("name")


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = factory.Faker("ean", length=8)
    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory(UserFactory)
    price = 1000
