class Category:
    def __init__(self, id_nember: int, name: str):
        self.id = id_nember
        self.name = name

    def edit(self, new_name: str):
        self.name = new_name
    
    def __repr__(self):
        return f"Category {self.id}: {self.name}"
