from homeworck_OOP_1.main.Product import Product


class Grass(Product):
    def __init__(self, name, description, price, quantity, country, period, color):
        super().__init__(name, description, price, quantity)
        self.productivity = country
        self.model = period
        self.color = color
