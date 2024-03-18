from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_obj(self, product_data):
        """Возвращает экземпляр класса Product"""
        pass


class Mixin:
    def __init__(self, *args, **kwargs):
        print(repr(self))

    def __repr__(self):
        a = ', '.join([f"{key}={value}" for key, value in self.__dict__.items()])
        return f'{self.__class__.__name__} {a}'


class Product(Mixin, AbstractProduct):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity
        super().__init__()
        # print(repr(self))

    def __str__(self):
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."

    # def __repr__(self):
    # return f"{self.__class__.__name__}{self.name, self.description, self._price, self.quantity}"

    def __add__(self, other):
        if type(other) is type(self):
            return (self.price * self.quantity) + (other.quantity * other.price)
        else:
            raise TypeError('Можно складывать объекты только одного класса')

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
