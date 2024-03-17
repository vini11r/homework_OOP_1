from homeworck_OOP_1.main.Product import Product


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, productivity, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.productivity = productivity
        self.model = model
        self.memory = memory
        self.color = color
        print(repr(self))
