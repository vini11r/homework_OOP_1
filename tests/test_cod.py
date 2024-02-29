import pytest
from main.Product import Product
from main.Category import Category


@pytest.fixture
def product():
    return Product('Samsung', 'Серый цвет', 180000.0, 5)


@pytest.fixture
def category():
    return Category('Смартфоны', 'Смартфоны, как', ['Samsung', 'Iphone', 'Xiaomi'])


def test_init_product(product):
    assert product.name == 'Samsung'
    assert product.description == 'Серый цвет'
    assert product.price == 180000.0
    assert product.quantity == 5


def test_init_category(category):
    assert category.name == 'Смартфоны'
    assert category.description == 'Смартфоны, как'
    assert category.products == ['Samsung', 'Iphone', 'Xiaomi']
    assert category.number_of_categories == 1
    assert category.number_of_products == 3
