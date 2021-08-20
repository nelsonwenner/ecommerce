from pytest_factoryboy import register
import pytest

from tests.factories import (
  AddressFactory,
  CategoryFactory,
  CustomerFactory,
  ProductFactory
)

register(CustomerFactory)
register(AddressFactory)
register(CategoryFactory)
register(ProductFactory)

@pytest.fixture
def customer(db, customer_factory):
  new_customer = customer_factory.create()
  return new_customer

@pytest.fixture
def admin_user(db, customer_factory):
  new_customer = customer_factory.create(username='admin_test', is_staff=True, is_superuser=True)
  return new_customer

@pytest.fixture
def address(db, address_factory):
  new_address = address_factory.create()
  return new_address

@pytest.fixture
def category(db, category_factory):
  category = category_factory.create()
  return category

@pytest.fixture
def product(db, product_factory):
  product = product_factory.create()
  return product