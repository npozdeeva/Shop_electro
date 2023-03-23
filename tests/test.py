from scratch import Product
#import pytest

def test_apply_discount():
    product = Product("Смартфон", 10000, 20)
    assert product.apply_discount() == 8000.0


def test_calculate_total_price():
    product = Product("Смартфон", 10000, 20)
    assert product.calculate_total_price() ==20000


def test_is_integer():
    assert Product.is_integer(6) == True
    assert Product.is_integer(5.5) == False


def test_name_len_10():
    product = Product("Смартфон", 10000, 20)
    product2 = Product("СмартСмартфон", 10000, 20)
    assert len(product) <= 10
    assert len(product2.name) > 10

def test_instantiate_from_csv():
    Product.instantiate_from_csv()
    assert len(Product.product_all) == 5