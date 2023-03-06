from tests.facrtories import CategoryFactory, UserFactory, AdFactory
from pytest_factoryboy import register

pytest_plugins = "tests.fixtures"
register(CategoryFactory)
register(UserFactory)
register(AdFactory)
