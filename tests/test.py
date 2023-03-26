from scratch import Product
import pytest

def test_apply_discount():
    product = Product("Смартфон", 10000, 20)
    product.pay_rate = 0.8
    product.apply_discount()
    assert product.price == 8000.0


def test_calculate_total_price():
    product = Product("Смартфон", 10000, 20)
    assert product.calculate_total_price() ==200000


def test_is_integer():
    assert Product.is_integer(6) == True
    assert Product.is_integer(5.5) == False
    assert Product.is_integer(10.1) == False
    assert Product.is_integer(12.0) == True


def test_name_len_10():
    product = Product("Смартфон", 10000, 20)
    with pytest.raises(Exception):
        product.name = 'СмартСмартфон'


def test_instantiate_from_csv():
    Product.instantiate_from_csv()
    assert len(Product.product_all) == 5