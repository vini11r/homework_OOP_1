class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @classmethod
    def get_obj(cls, product_data):
        """Возвращает список объектов класса Product"""
        return cls(**product_data)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print(f"Некорректная цена")
        else:
            self._price = new_price
