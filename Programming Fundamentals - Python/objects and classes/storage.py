class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        
    def add_product(self, product):
        if len(self.storage) < self.capacity:
            self.storage.append(str(product))

    def get_products(self):
        return self.storage


storage = Storage(4)
storage.add_product(3)
storage.add_product(1)
storage.add_product("potato")
storage.add_product("tomato")
storage.add_product("bread")

print(storage.get_products())
