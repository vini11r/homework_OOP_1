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

    def __str__(self):
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        return f"{self.__class__.__name__}{self.name, self.description, self._price, self.quantity}"

    def __add__(self, other):
        return (self.price * self.quantity) + (other.quantity * other.price)

    @classmethod
    def get_obj(cls, product_data):
        """Возвращает экземпляр класса Product"""
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
