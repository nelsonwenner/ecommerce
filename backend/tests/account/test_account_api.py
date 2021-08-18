from rest_framework_simplejwt.tokens import RefreshToken
from core.apps.account.models import Customer
from rest_framework.test import APIClient
import pytest

@pytest.mark.parametrize(
  'username, email, password, validity',
  [
    ('user', 'test@mail.com', '12346', 201),
    ('user', 'test@mail.com', '', 400),
    ('user', '', '123456', 400),
  ]
)

@pytest.mark.django_db
def test_create_account(client, username, email, password, validity):
  response = client.post('/account/register',
    data = {
      'username': username,
      'email': email,
      'password': password,
    },
  )
  assert response.status_code == validity

@pytest.fixture
def api_client():
  user = Customer.objects.create_user(username='customer_test', 
  email='test1@mail.com', password='test@123')
  client = APIClient()
  refresh = RefreshToken.for_user(user)
  client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
  return client

@pytest.mark.django_db
def test_get_token(client, customer):
  response = client.post('/account/token', {
    'email': 'test@mail.com',
    'password': 'test@123',
  })
  assert response.status_code == 200

@pytest.mark.django_db
def test_create_address(api_client):
  response = api_client.post('/account/address', {
    'street': 'São Bartolomeu',
    'suite': '7541',
    'city': 'Teresina',
    'zipcode': '65040215',
    'phone': '5656556',
    'delivery_instructions': 'fdfdfdf'
  })
  assert response.status_code == 201