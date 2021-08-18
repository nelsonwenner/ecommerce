import pytest

def test_customer_str(customer):
  assert customer.__str__() == 'customer_test'

def test_customer_admin_str(admin_user):
  assert admin_user.__str__() == 'admin_test'
'''
def test_when_customer_email_has_not_been_input(customer_factory):
  with pytest.raises(ValueError) as e:
    customer_factory.create(email='')
  assert str(e.value) == 'Customer Account: You must provide an email address'

def test_when_customer_email_incorrect(customer_factory):
  with pytest.raises(ValueError) as e:
    customer_factory.create(email='test.com')
  assert str(e.value) == 'You must provide a valid email address'

def test_adminuser_email_not_staff(customer_factory):
  with pytest.raises(ValueError) as e:
    customer_factory.create(email='', is_superuser=True, is_staff=False)
  assert str(e.value) == 'Superuser must have is_staff=True'

def test_adminuser_email_not_superuser(customer_factory):
  with pytest.raises(ValueError) as e:
    customer_factory.create(email='test.com', is_superuser=False, is_staff=True)
  assert str(e.value) == 'Superuser must have is_superuser=True'
'''
def test_address_str(address):
  name = address.customer.username
  assert address.__str__() == name + ' Address'
