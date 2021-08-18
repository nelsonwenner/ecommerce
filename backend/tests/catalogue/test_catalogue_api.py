import pytest

@pytest.mark.django_db
def test_should_return_status_code_200_in_the_categories_list(client):
  response = client.get('/catalogue/categories')
  assert response.status_code == 200

@pytest.mark.django_db
def test_should_return_status_code_200_in_the_categories_detail(client, category):
  response = client.get(f'/catalogue/categories/{category.id}')
  assert response.status_code == 200

@pytest.mark.django_db
def test_should_return_status_code_200_in_the_products_list(client):
  response = client.get('/catalogue/products')
  assert response.status_code == 200

@pytest.mark.django_db
def test_should_return_status_code_200_in_the_products_detail(client, product):
  response = client.get(f'/catalogue/products/{product.id}')
  assert response.status_code == 200