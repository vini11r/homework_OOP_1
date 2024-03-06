from homeworck_OOP_1.main.Product import Product


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

    def add_product(self, obj_product):
        """Добавляет объект товара в список товаров"""
        self.__products.append(obj_product)
        Category.number_of_products += 1

    @property
    def products(self):
        """Возвращает список товаров с указанием цены и количества"""
        products = ""
        for i in self.__products:
            product = f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт.\n"
            products += product
        return products
