class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, milliliters):
        if milliliters <= self.size - self.quantity:
            self.quantity += milliliters

    def status(self):
        space_left = self.size - self.quantity
        return space_left


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
