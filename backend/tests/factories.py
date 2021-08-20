from core.apps.account.models import Customer, Address
from core.apps.catalogue.models import Category, Product
from faker import Faker
import factory

fake = Faker()

class CustomerFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = Customer

  email = 'test@mail.com'
  username = 'customer_test'
  password = 'test@123'
  is_active = True
  is_staff = False

  @classmethod
  def _create(cls, model_class, *args, **kwargs):
    manager = cls._get_manager(model_class)
    if 'is_superuser' in kwargs:
      return manager.create_superuser(*args, **kwargs)
    else:
      return manager.create_user(*args, **kwargs)

class AddressFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = Address

  customer = factory.SubFactory(CustomerFactory)
  phone = fake.phone_number()
  zipcode = fake.postcode()
  suite = fake.name()
  street = fake.street_address()
  city = fake.city_suffix()
  delivery_instructions = fake.text()

class CategoryFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = Category

  name = 'django'

class ProductFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = Product

  category = factory.SubFactory(CategoryFactory)
  title = 'product_title'
  description = fake.text()
  image = fake.text()
  regular_price = '10.99'
  discount_price = '2.99'