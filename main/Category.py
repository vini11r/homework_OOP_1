from homeworck_OOP_1.main.Product import Product
from homeworck_OOP_1.main.Grass import Grass
from homeworck_OOP_1.main.Smartphone import Smartphone


class Category:
    name: str
    description: str
    products: list
    number_of_categories = 0
    number_of_products = 0

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.__products = product

        Category.number_of_categories += 1
        Category.number_of_products += len(self.__products)

    def __repr__(self):
        return f"{self.__class__.__name__}{self.name, self.description, self.__products}"

    def __len__(self):
        country_product = 0
        for i in self.__products:
            country_product += i.quantity
        return country_product

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)} шт."

    def add_product(self, obj_product):
        """Добавляет объект товара в список товаров"""
        if isinstance(obj_product, Product):
            self.__products.append(obj_product)
            Category.number_of_products += 1
        else:
            raise TypeError('Ошибка объекта продукта')

    @property
    def products(self):
        """Возвращает список товаров с указанием цены и количества"""
        products = ""
        for i in self.__products:
            # product = f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт.\n"
            products += f"{str(i)}\n"
        return products
