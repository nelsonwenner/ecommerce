import pytest

def test_category_str(category):
  assert category.__str__() == 'django'

def test_product_str(product):
  assert product.__str__() == 'product_title'